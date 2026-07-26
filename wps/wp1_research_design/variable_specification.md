# Variable Specification

Status: 2026-07-26. See `docs/research_design/research_design_by_claude.md`
Section 6 for full context.

## Dependent Variables

| Variable | Stage | Source | Operationalisation |
|---|---|---|---|
| Climate-Target Ambition Score | 1 | A (reports) | Composite 0–15 (provisional) across 5 criteria — see `wp3_reporting_quality/scoring_model.md` |
| Disclosure Quality Score (DQS) | 2 / panel | A (reports) | Composite 0–15 across 5 ESRS dimensions |
| ESRS Coverage Rate | 2 / panel | A (reports) | Share of mandatory ESRS data points disclosed |
| Double Materiality Completeness | 2 / panel | A (reports) | Binary/ordinal coding of impact + financial materiality |
| Assurance Status | 2 / panel | A (reports) | None / limited / reasonable |

## Independent Variables

| Variable | Stage | Source | Operationalisation |
|---|---|---|---|
| Mandatory vs. voluntary ESRS status | 1 | Country transposition status | Binary, derived from CSRD transposition tracker at FY2024 reporting date |
| Climate-Target Ambition Score / DQS | 2 | A (reports, from Stage 1/panel coding) | Continuous, used as regressor on market/risk outcomes |

## Control Variables

| Variable | Source | Notes |
|---|---|---|
| Firm size (log total assets) | B (Datastream) | |
| Leverage | B (Datastream) | |
| ROA, ROE, revenue growth | B (Datastream) | |
| Sector fixed effects | B (Datastream, ICB) | pending mapping to GICS |
| Country fixed effects | B (Datastream) | |
| Analyst coverage | B (Datastream) | proxy for external scrutiny, Stage 2 only |

## Moderators / Mediators

| Variable | Applies to | Notes |
|---|---|---|
| Firm size (large vs. mid-cap) | H5 (RQ4) | |
| Industry carbon intensity | H5 (RQ4) | |
| Country-level implementation status | H5 (RQ4) | |
| Analyst coverage | RQ3 (Stage 2) | proxy for external scrutiny |

## Benchmark Variables (Stage 1 ambition criteria)

| Variable | Source |
|---|---|
| Sector 1.5°C pathway (reduction pace benchmark) | SBTi / IEA / TPI — see `wp4_indicators/indicator_selection.md` |
| Firm's own historical emissions trend | Derived from report time series / Source B where available |
