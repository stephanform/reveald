# Sample Definition

Status: 2026-07-26. Two distinct samples, corresponding to the two data
sources (see `wp2_data_acquisition/data_sources.md`). See
`docs/research_design/research_design_by_claude.md` Section 5 for full
rationale — they are not merged into a single firm-year panel except at the
scoring/linkage step for Stage 2.

---

## A. Primary source (Source A — reports)

### A.1 Acquisition pool (WP2 coverage pool)
- **~1,056 EU-listed/registered companies** with at least one report or ESEF
  package retrieved, per `WORKING_NOTES.md` / `FEHLENDE_BERICHTE_MANUELL.md`
  (status 2026-07-24).
- Materials: PDF annual reports, standalone/integrated sustainability reports,
  ESEF/iXBRL packages.
- Sources: Bundesanzeiger/Unternehmensregister, national OAMs, Sustainability
  Reporting Navigator (SRN), company IR pages (see
  `data/sources/SUSTAINABILITY_REPORT_SOURCES.md`).
- Fiscal-year coverage varies by company; systematic ESEF availability begins
  FY2020; remaining gaps tracked in `FEHLENDE_BERICHTE_MANUELL.md`.
- This is a WP2 acquisition asset, not the Stage 1 coding sample itself.
  Over-representation of mature, sustained disclosers further back in time is
  treated as a scope condition on generalisability, not a bias to correct.

### A.2 Stage 1 coding sample (mandatory vs. voluntary comparison)
Drawn from A.1, restricted to FY2024 reports:
- **Mandatory group**: companies domiciled in EU Member States with completed
  CSRD transposition as of FY2024 reporting.
- **Voluntary group**: companies domiciled in Member States where
  transposition was still pending at FY2024 reporting (incl. Germany), that
  nonetheless reported ESRS-aligned climate targets.
- Sizing/balancing: to be finalised by cross-matching
  `data/raw/CSRD_Transposition_Tracker.xlsx` against A.1; target is a
  matched-pairs or stratified design (country, industry, firm size) rather
  than a large-N panel.

---

## B. Secondary source (Source B — LSEG Datastream)

Used for Stage 2 (market pricing) and the broader WP5/WP6 disclosure-quality
panel (RQ2/RQ4).

Companies listed in LSEG Datastream, status 2026-04-28, filtered by Navigator
using selection criteria:
- Category: Equities
- Market: [EU countries]
- Type: Equity
- Activity: Active (!)
- Security: Major
- Quote: Primary
- other criteria: no selection

### Geographical Scope
- 27 EU Countries
- European non-EU countries
- EU accession countries

### Industry Scope
- no delimitation at sampling stage; industry fixed effects applied at
  estimation stage via ICB sector labels

### Index / Universe
- Working file: `data/raw/reveald_sample_datastream.csv`

### Temporal Delimitation
- time frame from 2015 to 2025
- Intervention 1: NFRD entry into force 2017
- Intervention 2: CSRD entry into force 2024