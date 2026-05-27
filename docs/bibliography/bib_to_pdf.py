"""
bib_to_pdf.py
-------------
Converts a BibTeX (.bib) file into a Harvard-style PDF bibliography.

Usage:
    python bib_to_pdf.py                        # references.bib → references.pdf
    python bib_to_pdf.py my_refs.bib            # my_refs.bib   → my_refs.pdf
    python bib_to_pdf.py my_refs.bib output.pdf # explicit output path

Requires:
    pip install pybtex reportlab

Supported entry types: article, book, inbook, incollection,
                        inproceedings, misc, phdthesis, techreport
"""

import sys
import re
from pathlib import Path
from pybtex.database import parse_file

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Register Latin Modern Roman (Computer Modern successor) ───────────────────
# Latin Modern is the high-quality OpenType successor to Knuth's Computer Modern,
# used by virtually all current LaTeX journals.
#
# ReportLab only supports TrueType-outline fonts, not CFF/PostScript OTF.
# The TTF versions in ./fonts/ were pre-converted from the TeX Live OTF files
# using: otf2ttf -o fonts/LMRoman.ttf lmroman10-regular.otf  (etc.)
#
# To regenerate them yourself (requires otf2ttf from fonttools):
#   pip install fonttools
#   LM=/usr/share/texmf/fonts/opentype/public/lm
#   otf2ttf -o fonts/LMRoman.ttf            $LM/lmroman10-regular.otf
#   otf2ttf -o fonts/LMRoman-Bold.ttf       $LM/lmroman10-bold.otf
#   otf2ttf -o fonts/LMRoman-Italic.ttf     $LM/lmroman10-italic.otf
#   otf2ttf -o fonts/LMRoman-BoldItalic.ttf $LM/lmroman10-bolditalic.otf

_SCRIPT_DIR = Path(__file__).parent
_FONT_DIR   = _SCRIPT_DIR / 'fonts'
_LM_FONTS   = {
    'LMRoman':            'LMRoman.ttf',
    'LMRoman-Bold':       'LMRoman-Bold.ttf',
    'LMRoman-Italic':     'LMRoman-Italic.ttf',
    'LMRoman-BoldItalic': 'LMRoman-BoldItalic.ttf',
}

_LM_AVAILABLE = all((_FONT_DIR / f).exists() for f in _LM_FONTS.values())

if _LM_AVAILABLE:
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    for name, filename in _LM_FONTS.items():
        pdfmetrics.registerFont(TTFont(name, str(_FONT_DIR / filename)))
    registerFontFamily(
        'LMRoman',
        normal='LMRoman',
        bold='LMRoman-Bold',
        italic='LMRoman-Italic',
        boldItalic='LMRoman-BoldItalic',
    )
    BODY_FONT      = 'LMRoman'
    BODY_FONT_BOLD = 'LMRoman-Bold'
else:
    # Graceful fallback to built-in Times New Roman if TTF files are missing
    print("Note: Latin Modern TTF fonts not found in ./fonts/ — falling back to Times-Roman.")
    print("      See the comment above for how to generate the TTF files.")
    BODY_FONT      = 'Times-Roman'
    BODY_FONT_BOLD = 'Times-Bold'


# ── Colour palette ────────────────────────────────────────────────────────────
COL_TITLE    = HexColor('#1a1a2e')   # dark navy
COL_SUBTITLE = HexColor('#4a4a6a')   # muted purple-grey
COL_RULE     = HexColor('#ccccdd')   # light rule
COL_TEXT     = HexColor('#222222')   # near-black body text
COL_LINK     = HexColor('#1a5276')   # dark blue for DOI links


# ── Styles ────────────────────────────────────────────────────────────────────
# Uses Latin Modern Roman (Computer Modern successor) if available,
# otherwise falls back to Times-Roman.
def make_styles():
    return {
        'title': ParagraphStyle(
            'BibTitle',
            fontName=BODY_FONT_BOLD,
            fontSize=20,
            leading=26,
            textColor=COL_TITLE,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        'subtitle': ParagraphStyle(
            'BibSubtitle',
            fontName=BODY_FONT,
            fontSize=9,
            leading=13,
            textColor=COL_SUBTITLE,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        'entry': ParagraphStyle(
            'BibEntry',
            fontName=BODY_FONT,
            fontSize=11,
            leading=16,
            textColor=COL_TEXT,
            leftIndent=18,
            firstLineIndent=-18,   # hanging indent
            spaceAfter=8,
            alignment=TA_LEFT,
        ),
    }


# ── Helpers ───────────────────────────────────────────────────────────────────

def clean(text: str) -> str:
    """Remove LaTeX braces and basic commands."""
    text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
    text = re.sub(r'[{}]', '', text)
    text = text.replace('--', '–')
    # Escape ReportLab XML special chars
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return text.strip()


def get_field(entry, *keys) -> str:
    for key in keys:
        val = entry.fields.get(key, '')
        if val:
            return clean(val)
    return ''


def format_authors(persons) -> str:
    formatted = []
    for person in persons:
        last  = ' '.join(person.last_names)
        first = ' '.join(person.first_names + person.middle_names)
        initials = '.'.join(n[0] for n in re.split(r'[\s\-]+', first) if n) + '.' if first else ''
        last_clean  = clean(last)
        init_clean  = clean(initials)
        formatted.append(f"{last_clean}, {init_clean}" if init_clean else last_clean)

    if not formatted:
        return 'Anonymous'
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    return ', '.join(formatted[:-1]) + f" and {formatted[-1]}"


def doi_link(doi: str) -> str:
    """Return an HTML anchor tag for a DOI."""
    url = f"https://doi.org/{doi}"
    return f'<link href="{url}" color="{COL_LINK.hexval()}">doi: {doi}</link>'


# ── Entry formatters ──────────────────────────────────────────────────────────

def fmt_article(entry) -> str:
    authors  = format_authors(entry.persons.get('author', []))
    year     = get_field(entry, 'year')
    title    = get_field(entry, 'title')
    journal  = get_field(entry, 'journal')
    volume   = get_field(entry, 'volume')
    number   = get_field(entry, 'number')
    pages    = get_field(entry, 'pages')
    doi      = get_field(entry, 'doi')

    vol_issue = volume + (f"({number})" if number else "")

    ref = f"{authors} ({year}) '{title}', <i>{journal}</i>"
    if vol_issue:
        ref += f", {vol_issue}"
    if pages:
        ref += f", pp. {pages}"
    if doi:
        ref += f". {doi_link(doi)}"
    return ref + '.'


def fmt_book(entry) -> str:
    authors   = format_authors(entry.persons.get('author', []) or
                                entry.persons.get('editor', []))
    year      = get_field(entry, 'year')
    title     = get_field(entry, 'title')
    edition   = get_field(entry, 'edition')
    publisher = get_field(entry, 'publisher')
    address   = get_field(entry, 'address')

    ref = f"{authors} ({year}) <i>{title}</i>"
    if edition:
        ref += f", {edition} edn"
    ref += f". {publisher}"
    if address:
        ref += f", {address}"
    return ref + '.'


def fmt_incollection(entry) -> str:
    authors   = format_authors(entry.persons.get('author', []))
    year      = get_field(entry, 'year')
    title     = get_field(entry, 'title')
    booktitle = get_field(entry, 'booktitle')
    editors   = format_authors(entry.persons.get('editor', []))
    pages     = get_field(entry, 'pages')
    publisher = get_field(entry, 'publisher')
    address   = get_field(entry, 'address')

    ref = f"{authors} ({year}) '{title}'"
    if booktitle:
        ref += f", in {editors} (ed.) <i>{booktitle}</i>" if editors else f", in <i>{booktitle}</i>"
    if pages:
        ref += f", pp. {pages}"
    ref += f". {publisher}"
    if address:
        ref += f", {address}"
    return ref + '.'


def fmt_inproceedings(entry) -> str:
    authors   = format_authors(entry.persons.get('author', []))
    year      = get_field(entry, 'year')
    title     = get_field(entry, 'title')
    booktitle = get_field(entry, 'booktitle')
    pages     = get_field(entry, 'pages')
    address   = get_field(entry, 'address')

    ref = f"{authors} ({year}) '{title}', <i>{booktitle}</i>"
    if pages:
        ref += f", pp. {pages}"
    if address:
        ref += f", {address}"
    return ref + '.'


def fmt_phdthesis(entry) -> str:
    authors = format_authors(entry.persons.get('author', []))
    year    = get_field(entry, 'year')
    title   = get_field(entry, 'title')
    school  = get_field(entry, 'school')
    return f"{authors} ({year}) <i>{title}</i>. PhD thesis, {school}."


def fmt_techreport(entry) -> str:
    authors     = format_authors(entry.persons.get('author', []))
    year        = get_field(entry, 'year')
    title       = get_field(entry, 'title')
    institution = get_field(entry, 'institution')
    number      = get_field(entry, 'number')

    ref = f"{authors} ({year}) <i>{title}</i>. Technical Report"
    if number:
        ref += f" {number}"
    return ref + f", {institution}."


def fmt_misc(entry) -> str:
    authors = format_authors(entry.persons.get('author', []))
    year    = get_field(entry, 'year')
    title   = get_field(entry, 'title')
    url     = get_field(entry, 'url')
    note    = get_field(entry, 'note')

    ref = f"{authors} ({year}) <i>{title}</i>"
    if note:
        ref += f". {note}"
    if url:
        ref += f". Available at: <link href='{url}' color='{COL_LINK.hexval()}'>{url}</link>"
    return ref + '.'


FORMATTERS = {
    'article':       fmt_article,
    'book':          fmt_book,
    'inbook':        fmt_incollection,
    'incollection':  fmt_incollection,
    'inproceedings': fmt_inproceedings,
    'conference':    fmt_inproceedings,
    'phdthesis':     fmt_phdthesis,
    'techreport':    fmt_techreport,
    'misc':          fmt_misc,
}


def format_entry(key: str, entry) -> str:
    etype = entry.type.lower()
    formatter = FORMATTERS.get(etype, fmt_misc)
    try:
        return formatter(entry)
    except Exception as exc:
        return f"[Could not format entry '{key}': {exc}]"


def sort_key(item):
    key, entry = item
    persons = entry.persons.get('author', []) or entry.persons.get('editor', [])
    last = persons[0].last_names[0].lower() if persons else 'zzz'
    year = get_field(entry, 'year') or '0000'
    return (last, year)


# ── Main ──────────────────────────────────────────────────────────────────────

def convert(bib_path: Path, pdf_path: Path):
    bib_data = parse_file(str(bib_path))
    entries  = sorted(bib_data.entries.items(), key=sort_key)
    styles   = make_styles()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
        title='Bibliography',
        author='bib_to_pdf.py',
    )

    story = []

    # Header
    story.append(Paragraph("Bibliography", styles['title']))
    story.append(Paragraph(
        f"Generated from <i>{bib_path.name}</i> — Harvard (author-date) style",
        styles['subtitle']
    ))
    story.append(HRFlowable(width='100%', thickness=1, color=COL_RULE, spaceAfter=14))

    # Entries
    for key, entry in entries:
        html = format_entry(key, entry)
        story.append(Paragraph(html, styles['entry']))

    # Footer rule
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width='100%', thickness=0.5, color=COL_RULE))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        f"{len(entries)} reference{'s' if len(entries) != 1 else ''}",
        styles['subtitle']
    ))

    doc.build(story)
    print(f"✓ Written {len(entries)} reference(s) to '{pdf_path}'")


if __name__ == '__main__':
    args = sys.argv[1:]

    bib_path = Path(args[0]) if len(args) >= 1 else Path('references.bib')
    pdf_path = Path(args[1]) if len(args) >= 2 else bib_path.with_suffix('.pdf')

    if not bib_path.exists():
        print(f"Error: '{bib_path}' not found.")
        sys.exit(1)

    convert(bib_path, pdf_path)
