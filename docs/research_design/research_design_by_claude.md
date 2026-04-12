# REVEALD – Research Design
**Regulatory Evaluation of ESG-Aligned Disclosure**

Bremen University of Applied Sciences (HSB) · Faculty Fk1 (Business) · DTX Research Cluster Project  · Project Lead: Prof. Dr. Stephan Form · ORCID: 0009-0008-1396-4323

Last updated: April 2026

---

## Table of Contents

1. [Background](#1-background)
2. [Research Questions & Hypotheses](#2-research-questions--hypotheses)
3. [Study Design](#3-study-design)
4. [Sample Definition](#4-sample-definition)
5. [Variables](#5-variables)
6. [Data Sources](#6-data-sources)
7. [Disclosure Quality Scoring Model (DQS)](#7-disclosure-quality-scoring-model-dqs)
8. [Analytical Strategy](#8-analytical-strategy)
9. [Quality Assurance & Research Governance](#9-quality-assurance--research-governance)
10. [Limitations](#10-limitations)
11. [Timeline](#11-timeline)

---

## 1. Background

To support the transformation towards a climate-neutral and resource-efficient
economy, the European Commission revised the Non-Financial Reporting Directive
(NFRD, Directive (EU) 2014/95) through the Corporate Sustainability Reporting
Directive (CSRD, Directive (EU) 2022/2464) and the European Sustainability
Reporting Standards (ESRS).

The effectiveness of the CSRD is subject to a structural tension for two reasons:

- Not all Member States have transposed the Directive into national law; as of
  end of 2025, implementation was still pending in seven countries, including
  Germany.
- The CSRD regulations are to be delayed and enter into force in a weakened form
  through Directive (EU) 2025/794 ("Stop the Clock").

As a result, a unique dataset emerges for capital-market-oriented accounting
research: within a relatively homogeneous legal environment, CSRD-compliant
annual reports are available for a subset of companies, while they are not
available for others. REVEALD exploits this natural variation to assess the
causal effect of sustainability reporting regulation.

---

## 2. Research Questions & Hypotheses

### Research Questions

**RQ1 (Dynamics)**
To what extent has the transition from NFRD to CSRD/ESRS regulation improved
the quality and comprehensiveness of corporate sustainability reporting?

**RQ2 (Tensions)**
How does increasing sustainability disclosure regulation interact with corporate
financial performance, competitiveness, and risk-bearing capacity?

**RQ3 (Comparative)**
How do reporting quality and sustainability indicator development vary across
countries, industries, and regulatory exposure groups?

### Hypotheses

| # | Hypothesis |
|---|---|
| H1 | Companies subject to CSRD-compliant reporting requirements exhibit significantly higher disclosure quality scores than companies in the control group. |
| H2 | The positive effect of CSRD compliance on disclosure quality is moderated by firm size, industry affiliation, and country-level implementation status. |
| H3 | Higher disclosure quality is associated with measurable improvements in sustainability indicators (e.g. emissions intensity, energy intensity) over time. |
| H4 | The relationship between disclosure quality and financial performance (ROA/ROE) is non-linear, reflecting short-term compliance costs versus long-term value effects. |

---

## 3. Study Design

A **quasi-experimental longitudinal panel design** combining
difference-in-differences (DiD) with content analysis is used. This exploits
the natural variation in CSRD implementation timing across EU Member States as
an exogenous shock.

| Design Element | Specification |
|---|---|
| Design type | Quasi-experimental, longitudinal |
| Time horizon | 2015–2024 (approx. 10 reporting years) |
| Treatment group | CSRD-compliant reporters from 2024 onwards |
| Control group | Non-compliant companies in same industries/countries |
| Unit of analysis | Firm–year observations |
| Level of analysis | Report-level + financial data |

---

## 4. Sample Definition

### Geographical Scope

- EU Member States with completed CSRD transposition (treatment-eligible) vs.
  those where transposition is still pending, including Germany (natural control
  pool)
- Target: 6–8 countries balancing transposition status, market size, and data
  availability

### Industry Scope

At minimum: financial services, manufacturing, energy/utilities, retail —
sectors with high sustainability relevance and reporting maturity variation.

### Index / Universe

- Capital-market-oriented companies; starting from STOXX Europe 600 or
  equivalent, filtered by reporting availability
- Target panel size: **200–400 firm–year observations**

---

## 5. Variables

### Dependent Variables

| Variable | Operationalisation |
|---|---|
| Disclosure Quality Score (DQS) | Composite scoring model across ESRS dimensions (see Section 7) |
| ESRS Coverage Rate | Share of mandatory ESRS data points disclosed |
| Double Materiality Completeness | Binary/ordinal coding of impact + financial materiality |
| Assurance Status | None / limited / reasonable |

### Key Sustainability Indicators (Outcomes)

- Emissions intensity (Scope 1+2 per revenue/FTE)
- Energy intensity
- Target pathway disclosure (science-based targets, net zero)
- Social indicators (if data permits): gender pay gap, workforce turnover

### Financial / Performance Variables

- ROA, ROE, revenue growth
- Leverage, firm size (log total assets), market-to-book
- Sector and country fixed effects

### Moderators / Mediators (Tensions Dimension)

- Firm size (large vs. mid-cap)
- Industry carbon intensity
- Analyst coverage (proxy for external scrutiny)

---

## 6. Data Sources

| Data Type | Source |
|---|---|
| Sustainability / annual reports | Company IR pages (AI-assisted retrieval), ESEF filings |
| ESG data (validation / benchmarking) | Refinitiv/LSEG, Bloomberg ESG, or S&P Trucost |
| Financial indicators | Compustat Global, Refinitiv Datastream |
| Regulatory implementation status | EUR-Lex, national transposition tracker |
| Industry classification | NACE Rev. 2 / GICS |

---

## 7. Disclosure Quality Scoring Model (DQS)

The DQS is the analytical centrepiece of the project (WP3). It covers five
dimensions, each scored on a **0–3 ordinal scale**, yielding a composite score
of **0–15**.

| Dimension | Description | Scale |
|---|---|---|
| 1. Coverage | Share of ESRS topical standards addressed (E1–E5, S1–S4, G1) | 0–3 |
| 2. Granularity | Qualitative vs. quantitative disclosure; presence of metrics and targets | 0–3 |
| 3. Double Materiality | Explicit documentation of impact materiality and financial materiality | 0–3 |
| 4. Forward-looking Orientation | Presence of targets, pathways, scenario analysis | 0–3 |
| 5. Assurance | External verification status and scope | 0–3 |
| **Total DQS** | | **0–15** |

### Intercoder Reliability

Inter-coder reliability is assessed via **Cohen's Kappa** during the pilot
coding phase (20–30 reports).

- Target: **κ ≥ 0.70**
- Disagreements resolved through structured discussion and coding manual updates
  before the main coding phase begins

---

## 8. Analytical Strategy

### Phase 1 — Descriptive & Longitudinal Analysis (WP5)

- Time-series plots of DQS and sustainability indicators (2015–2024)
- Structural break tests around NFRD (2018) and CSRD (2024) introduction
- Country and industry heatmaps of reporting maturity

### Phase 2 — Causal Identification (WP6)

#### Difference-in-Differences (DiD) — Main Specification

$$DQS_{it} = \alpha + \beta_1 \cdot Treated_i + \beta_2 \cdot Post_t + \beta_3 \cdot (Treated_i \times Post_t) + \gamma X_{it} + \delta_i + \lambda_t + \varepsilon_{it}$$

Where:

| Symbol | Definition |
|---|---|
| $DQS_{it}$ | Disclosure Quality Score for firm $i$ in year $t$ |
| $Treated_i$ | 1 if firm is subject to CSRD, 0 otherwise |
| $Post_t$ | 1 for years after CSRD entry into force |
| $\beta_3$ | **Key treatment effect** (DiD estimator) |
| $X_{it}$ | Firm-level control variables |
| $\delta_i$ | Firm fixed effects |
| $\lambda_t$ | Year fixed effects |
| $\varepsilon_{it}$ | Error term |

#### Extensions

- **Staggered DiD** — accounts for variation in CSRD transposition timing across
  countries
- **Event study** — visualises pre-trends and dynamic treatment effects to
  validate parallel trends assumption
- **Moderation analysis** — tests Tensions hypothesis via interaction term
  (DQS × financial performance)
- **Robustness checks** — alternative DQS weightings, winsorisation at 1%/99%,
  placebo tests, alternative lag structures

#### Software

- **R** (primary): `fixest`, `did`, `tidyverse`
- Replication-ready scripts in `wp6_estimation/scripts/`

---

## 9. Quality Assurance & Research Governance

| Element | Specification |
|---|---|
| Coding manual | Decision rules and anchor examples documented in `wp2_data_acquisition/coding_manual/` |
| Intercoder reliability | Pilot on 20–30 reports; discrepancies resolved before main coding |
| Data versioning | Timestamped raw data snapshots; documented transformation steps |
| Reproducibility package | Data dictionary, codebook, R scripts, README in `reproducibility_package/` |
| Licensed data | Excluded from version control via `.gitignore`; access instructions in `wp2_data_acquisition/data_governance.md` |

---

## 10. Limitations

| Limitation | Mitigation Strategy |
|---|---|
| Self-selection into early CSRD compliance | Firm fixed effects + robustness tests |
| Incomplete transposition creating legal ambiguity | Sensitivity analysis excluding borderline cases |
| AI-assisted extraction errors | Manual spot-checks on 10% of coded reports |
| Short post-treatment window (2024 only at project start) | Frame as first-wave evidence; note need for longitudinal follow-up |
| Potential greenwashing / symbolic disclosure | Disclosure-performance gap analysis as robustness check |

---

## 11. Timeline

| Month | Work Package | Key Milestone |
|---|---|---|
| 1–2 | WP1 | RQs, hypotheses, sample, variable specification finalised |
| 2–4 | WP2 | Document corpus built; panel structure established |
| 3–6 | WP3 | DQS scoring model finalised; pilot + main coding completed |
| 4–7 | WP4 | Financial/sustainability data merged; missing-data report |
| 6–8 | WP5 | Descriptive analyses, structural break tests, country/industry profiles |
| 7–10 | WP6 | DiD estimation, event studies, robustness checks |
| 10–12 | WP7 | Conference paper submitted; reproducibility package delivered |

---

## References

> See `docs/bibliography/reveald.bib` for the full BibTeX reference list.

Key references for this research design:

- Aluchna, M. et al. (2023). From Talk to Action: The Effects of the
  Non-Financial Reporting Directive on ESG Performance.
  *Meditari Accountancy Research.*
- Christensen, H.B. et al. (2024). Mandatory versus Voluntary Non-Financial
  Reporting. *Accounting and Business Research.*
- Dinh, T., Husmann, A., & Melloni, G. (2024). An Overview of Corporate
  Sustainability Reporting Legislation in the European Union.
  *Accounting in Europe.*
- Krueger, P. et al. (2024). The Effects of Mandatory ESG Disclosure Around
  the World. *Journal of Accounting Research.*
- Radu, O.M., Dragomir, V.D. & Hao, N. (2023). Company-Level Factors of
  Non-Financial Reporting Quality under a Mandatory Regime.
  *Sustainability (MDPI).*

---

*REVEALD · Bremen University of Applied Sciences · Faculty Fk1 (Business)*
