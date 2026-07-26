# Data Governance

Status: 2026-07-26.

## Versioning Rules

- **Source A (reports)**: raw PDFs/ESEF packages retrieved are kept as
  downloaded, filed per company; acquisition status tracked in
  `data/raw/primary/WORKING_NOTES.md` and gaps in
  `FEHLENDE_BERICHTE_MANUELL.md`, both timestamped at each update.
- **Source B (LSEG Datastream)**: each pull is saved as a dated snapshot
  (`reveald_sample_datastream_<date/scope>.csv`); the pull-date used for any
  given analysis must be recorded in the corresponding WP6 script/output, since
  vendor restatements and backfilling can change historical values between
  pulls.
- Derived/processed files (coded scores, merged panels) are written to
  `data/processed/` and must document which raw snapshot(s) and coding-manual
  version they derive from.

## Reproducibility Protocol

- Coding decisions (DQS, Climate-Target Ambition Score) follow the anchor
  examples and decision rules in `wp2_data_acquisition/coding_manual/` and
  `wp3_reporting_quality/scoring_model.md`; manual updates during pilot coding
  are version-noted.
- Analysis scripts (R: `fixest`, `did`, `tidyverse`) live in
  `wp6_estimation/scripts/` and are expected to run against a specific,
  documented Source B pull-date.
- Final replication materials (data dictionary, codebook, scripts, README) are
  assembled in `reproducibility_package/` ahead of journal submission.

## Access Instructions for Licensed Data

- LSEG Datastream (Refinitiv) data is licensed and excluded from version
  control via `.gitignore`; it is not redistributed as part of this
  repository or the reproducibility package. Access requires an active
  institutional Refinitiv/LSEG license (HSB or partner institution).
- Source A materials (company reports, ESEF packages) are public disclosures
  and are not subject to the same licensing restriction, but are also kept
  outside version control to limit repository size; retrieval sources and
  methods are documented in `data/sources/SUSTAINABILITY_REPORT_SOURCES.md`
  and `data/raw/primary/WORKING_NOTES.md` so the corpus can be re-acquired
  independently.
