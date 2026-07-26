# Data Sources

Status: 2026-07-26. Full definitions, methodological classification, and
limitations are in `docs/research_design/research_design_by_claude.md`
Section 7. This file indexes the concrete files/locations.

## Source A — Sustainability / Annual Reports (primary source documents)

- Acquisition pool: ~1,056 EU companies, PDF annual reports + standalone/
  integrated sustainability reports + ESEF/iXBRL packages
  (`data/raw/primary/`, see `WORKING_NOTES.md`, `FEHLENDE_BERICHTE_MANUELL.md`)
- Aggregators/registers checked and their coverage limits:
  `data/sources/SUSTAINABILITY_REPORT_SOURCES.md`
- Classification: primary source document (unmediated, direct from
  disclosing entity); used for qualitative content analysis (Stage 1 Ambition
  Score, DQS panel coding)

## Source B — ESG / Financial Data Provider (secondary, compiled data)

- LSEG Datastream (Refinitiv), firm-level panel: financials, ESG indicators,
  ICB sector labels — `data/raw/reveald_sample_datastream.csv` and
  country/topic-specific extracts in the same folder
- Classification: secondary (compiled/derived) data — vendor-mediated; used
  for Stage 2 market-pricing association and the broader disclosure-quality
  panel (WP5/WP6)

## Benchmark Sources (Stage 1 ambition scoring)

- Science Based Targets initiative (SBTi) sector pathways
- International Energy Agency (IEA) sector pathways
- Transition Pathway Initiative (TPI)

## Regulatory & Classification Sources

- EUR-Lex; national CSRD transposition tracker
  (`data/raw/CSRD_Transposition_Tracker.xlsx`, `CSRD_Umsetzung.xlsx`)
- Industry classification: NACE Rev. 2 / ICB / GICS
