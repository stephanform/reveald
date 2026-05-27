"""
bib_to_md.py
------------
Converts a BibTeX (.bib) file into a Harvard-style Markdown bibliography.

Usage:
    python bib_to_md.py                        # uses references.bib → references.md
    python bib_to_md.py my_refs.bib            # uses my_refs.bib   → my_refs.md
    python bib_to_md.py my_refs.bib output.md  # explicit output path

Supported entry types: article, book, inbook, incollection,
                        inproceedings, misc, phdthesis, techreport
"""

import sys
import re
from pathlib import Path
from pybtex.database import parse_file


# ── Helpers ───────────────────────────────────────────────────────────────────

def clean(text: str) -> str:
    """Remove LaTeX braces and basic commands from a field value."""
    text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)  # \cmd{x} → x
    text = re.sub(r'[{}]', '', text)                          # bare braces
    text = text.replace('--', '–')                            # en-dash for page ranges
    return text.strip()


def get_field(entry, *keys) -> str:
    """Return the first matching field value, or empty string."""
    for key in keys:
        val = entry.fields.get(key, '')
        if val:
            return clean(val)
    return ''


def format_authors(persons) -> str:
    """
    Format a list of pybtex Person objects into Harvard style.
    Single author:   Smith, J.
    Two authors:     Smith, J. and Jones, A.
    Three or more:   Smith, J., Jones, A. and Brown, C.
    """
    formatted = []
    for person in persons:
        last  = ' '.join(person.last_names)
        first = ' '.join(person.first_names + person.middle_names)
        # Abbreviate first/middle names to initials
        initials = '.'.join(n[0] for n in re.split(r'[\s\-]+', first) if n) + '.' if first else ''
        formatted.append(f"{last}, {initials}" if initials else last)

    if len(formatted) == 0:
        return 'Anonymous'
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    return ', '.join(formatted[:-1]) + f" and {formatted[-1]}"


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

    vol_issue = volume
    if number:
        vol_issue += f"({number})"

    ref = f"{authors} ({year}) '{title}', *{journal}*"
    if vol_issue:
        ref += f", {vol_issue}"
    if pages:
        ref += f", pp. {pages}"
    if doi:
        ref += f". doi: [{doi}](https://doi.org/{doi})"
    ref += '.'
    return ref


def fmt_book(entry) -> str:
    authors   = format_authors(entry.persons.get('author', []) or
                                entry.persons.get('editor', []))
    year      = get_field(entry, 'year')
    title     = get_field(entry, 'title')
    edition   = get_field(entry, 'edition')
    publisher = get_field(entry, 'publisher')
    address   = get_field(entry, 'address')

    ref = f"{authors} ({year}) *{title}*"
    if edition:
        ref += f", {edition} edn"
    ref += f". {publisher}"
    if address:
        ref += f", {address}"
    ref += '.'
    return ref


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
        ref += f", in {editors} (ed.) *{booktitle}*" if editors else f", in *{booktitle}*"
    if pages:
        ref += f", pp. {pages}"
    ref += f". {publisher}"
    if address:
        ref += f", {address}"
    ref += '.'
    return ref


def fmt_inproceedings(entry) -> str:
    authors   = format_authors(entry.persons.get('author', []))
    year      = get_field(entry, 'year')
    title     = get_field(entry, 'title')
    booktitle = get_field(entry, 'booktitle')
    pages     = get_field(entry, 'pages')
    address   = get_field(entry, 'address')

    ref = f"{authors} ({year}) '{title}', *{booktitle}*"
    if pages:
        ref += f", pp. {pages}"
    if address:
        ref += f", {address}"
    ref += '.'
    return ref


def fmt_phdthesis(entry) -> str:
    authors = format_authors(entry.persons.get('author', []))
    year    = get_field(entry, 'year')
    title   = get_field(entry, 'title')
    school  = get_field(entry, 'school')

    return f"{authors} ({year}) *{title}*. PhD thesis, {school}."


def fmt_techreport(entry) -> str:
    authors     = format_authors(entry.persons.get('author', []))
    year        = get_field(entry, 'year')
    title       = get_field(entry, 'title')
    institution = get_field(entry, 'institution')
    number      = get_field(entry, 'number')

    ref = f"{authors} ({year}) *{title}*. Technical Report"
    if number:
        ref += f" {number}"
    ref += f", {institution}."
    return ref


def fmt_misc(entry) -> str:
    authors = format_authors(entry.persons.get('author', []))
    year    = get_field(entry, 'year')
    title   = get_field(entry, 'title')
    url     = get_field(entry, 'url')
    note    = get_field(entry, 'note')

    ref = f"{authors} ({year}) *{title}*"
    if note:
        ref += f". {note}"
    if url:
        ref += f". Available at: <{url}>"
    ref += '.'
    return ref


# ── Dispatch ──────────────────────────────────────────────────────────────────

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
    """Sort by first author's last name, then year."""
    key, entry = item
    persons = entry.persons.get('author', []) or entry.persons.get('editor', [])
    last = persons[0].last_names[0].lower() if persons else 'zzz'
    year = get_field(entry, 'year') or '0000'
    return (last, year)


# ── Main ──────────────────────────────────────────────────────────────────────

def convert(bib_path: Path, md_path: Path):
    bib_data = parse_file(str(bib_path))

    entries = sorted(bib_data.entries.items(), key=sort_key)

    lines = [
        "# Bibliography\n",
        f"*Generated from `{bib_path.name}` — Harvard (author-date) style*\n",
        "---\n",
    ]

    for key, entry in entries:
        ref = format_entry(key, entry)
        lines.append(f"- {ref}\n")

    md_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"✓ Written {len(entries)} reference(s) to '{md_path}'")


if __name__ == '__main__':
    args = sys.argv[1:]

    bib_path = Path(args[0]) if len(args) >= 1 else Path('references.bib')
    md_path  = Path(args[1]) if len(args) >= 2 else bib_path.with_suffix('.md')

    if not bib_path.exists():
        print(f"Error: '{bib_path}' not found.")
        sys.exit(1)

    convert(bib_path, md_path)
