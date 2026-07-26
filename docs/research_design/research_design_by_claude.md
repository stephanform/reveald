# REVEALD – Research Design
**Regulatory Evaluation of ESG-Aligned Disclosure**

Bremen University of Applied Sciences (HSB) · Faculty Fk1 (Business) · DTX Research Cluster Project  · Project Lead: Prof. Dr. Stephan Form · ORCID: 0009-0008-1396-4323

Last updated: 2026-07-26

---

## Table of Contents

1. [Background](#1-background)
2. [Staged Research Strategy](#2-staged-research-strategy)
3. [Research Questions & Hypotheses](#3-research-questions--hypotheses)
4. [Study Design](#4-study-design)
5. [Sample Definition](#5-sample-definition)
6. [Variables](#6-variables)
7. [Data Sources](#7-data-sources)
8. [Disclosure Quality & Climate-Target Ambition Scoring](#8-disclosure-quality--climate-target-ambition-scoring)
9. [Analytical Strategy](#9-analytical-strategy)
10. [Quality Assurance & Research Governance](#10-quality-assurance--research-governance)
11. [Limitations](#11-limitations)
12. [Target Journals](#12-target-journals)
13. [Timeline](#13-timeline)
14. [References](#references)

---

## 1. Background

To support the transformation towards a climate-neutral and resource-efficient
economy, the European Commission revised the Non-Financial Reporting Directive
(NFRD, Directive (EU) 2014/95) through the Corporate Sustainability Reporting
Directive (CSRD, Directive (EU) 2022/2464) and the European Sustainability
Reporting Standards (ESRS).

The effectiveness of the CSRD is subject to a structural tension for two reasons:

- Not all Member States have transposed the Directive into national law; as of
  end of 2025, implementation was still pending in several countries, including
  Germany.
- The CSRD regulations are to be delayed and enter into force in a weakened form
  through Directive (EU) 2025/794 ("Stop the Clock").

As a result, a unique dataset emerges for accounting and sustainability
research: within a relatively homogeneous legal environment, ESRS-compliant
annual/sustainability reports are available for a subset of companies for
fiscal year 2024, while other companies in countries without national
transposition reported under ESRS voluntarily, or not at all. REVEALD exploits
this natural variation — mandatory vs. voluntary ESRS adoption — to assess
disclosure practices and, over the project's course, their relationship to
market and risk outcomes.

### Related work and positioning

Donau, Sellhorn et al. (2025), "Targeting Transparency: Early Evidence on
Mandatory Adoption of European Sustainability Reporting Standards," analyse
~1,000 EU companies applying ESRS for the first time in fiscal year 2024,
comparing them against similar non-EU firms to measure the *increase in the
volume* of disclosure attributable to ESRS. Backed by a large DFG-funded
research consortium, this paper is expected to anchor the top end of the
empirical literature on first-wave ESRS adoption.

REVEALD does not compete with this effect. Three gaps in Donau et al. define
our contribution instead:

1. They measure disclosure **quantity**, not the **content or ambition** of
   what is disclosed.
2. They compare EU vs. non-EU firms; they treat the **mandatory-vs-voluntary
   split within the EU** (arising from delayed national transposition,
   including Germany) only in passing.
3. They explicitly leave **capital-market consequences** of ESRS adoption for
   future research.

REVEALD is positioned to address gaps (1) and (2) immediately, and gap (3) in
a methodologically modest, correlational form as a second step (see Section 2).

---

## 2. Staged Research Strategy

The original REVEALD proposal centred on a single capital-market event study
around the CSRD's introduction. On review, a clean event-study design is not
viable for this regulatory shock: there is no single, unanticipated event date
(the regulatory process unfolded over several years and was largely
anticipated), the mandatory-vs-voluntary comparison used elsewhere in this
design cannot be mapped onto an event window (a country's non-transposition is
not a dateable market event), and the direct version of this test — disclosure
regulation and cost of capital — already exists for the NFRD (Grewal, Riedl &
Serafeim) and is a crowded field internationally.

REVEALD is therefore structured as three stages of increasing ambition, sharing
one data foundation:

| Stage | Question | Status | Data used |
|---|---|---|---|
| **Stage 1 — Ambition** | Are 2024 climate targets, reported for the first time in standardised ESRS form, actually more ambitious under mandatory disclosure, or only more uniformly formatted? | **This project — primary deliverable** | Source A (reports), qualitative/content-analytic coding |
| **Stage 2 — Market pricing** | Does the capital market price disclosure quality and climate-target ambition differently from vague disclosure? | This project — secondary deliverable, correlational | Stage 1 scores + Source B (LSEG Datastream), quantitative panel analysis |
| **Outlook — Target achievement** | Do firms subject to ESRS actually close in on their stated climate targets over time? | Future project (data requires ≥2026 reporting years); working title reserved via this project's Stage 1 dataset | Longitudinal extension of Source A, ideally with STARS-EU partners (Bragança, Opava) |

Framing Stage 2 as *correlational, not causal* is a deliberate and stated
scope limitation (see Section 11) — it substitutes for the abandoned
event-study approach and must not be over-claimed as a DiD-identified causal
estimate in the same sense as Stage 1's mandatory-vs-voluntary comparison.

Working title (Stage 1): *"Mandated but ambitious? Climate-target ambition
and credibility in the first wave of ESRS reports."*

---

## 3. Research Questions & Hypotheses

### Research Questions

**RQ1 (Ambition — Stage 1)**
Under the first mandatory wave of ESRS climate-target reporting (FY2024), are
targets more ambitious and more credible for companies reporting under legal
obligation than for companies reporting the same standardised target
structure voluntarily?

**RQ2 (Dynamics)**
To what extent has the transition from NFRD to CSRD/ESRS regulation improved
the quality and comprehensiveness of corporate sustainability reporting more
broadly (beyond climate targets)?

**RQ3 (Market Pricing — Stage 2)**
Is higher disclosure quality / climate-target ambition associated with
differences in firms' market valuation and risk indicators?

**RQ4 (Comparative)**
How do reporting quality and climate-target ambition vary across countries,
industries, and mandatory/voluntary regulatory exposure groups?

### Hypotheses

| # | Stage | Hypothesis |
|---|---|---|
| H1 | 1 | Climate targets reported by companies under mandatory ESRS disclosure are more ambitious (faster reduction pace relative to a 1.5°C sector pathway, greater departure from the firm's own historical trend) than those reported voluntarily. |
| H2 | 1 | Climate targets reported under mandatory disclosure more frequently cover value-chain (Scope 3) emissions and include near-term interim milestones, rather than a distant net-zero commitment alone. |
| H3 | 1 | Mandatory disclosure is associated with more concrete, less offset-reliant target design than voluntary disclosure (i.e., the mandate raises substantive ambition, not only formatting uniformity). |
| H4 | 2 | Companies with higher disclosure quality / climate-target ambition scores show different market valuation and risk-indicator profiles than companies with lower scores, controlling for size, leverage, and sector. |
| H5 | 4 | The effect of the mandatory/voluntary status on ambition (H1–H3) is moderated by firm size, industry carbon intensity, and country-level implementation status. |

H1–H3 are the primary, immediately testable hypotheses (Stage 1, this
project's main deliverable). H4 is exploratory and correlational (Stage 2).
H5 supports RQ4.

---

## 4. Study Design

REVEALD combines two design components, mapped onto the staged strategy in
Section 2:

| Design Element | Stage 1 (Ambition) | Stage 2 (Market Pricing) |
|---|---|---|
| Design type | Cross-sectional comparative content analysis | Correlational cross-sectional / short panel |
| Comparison | Mandatory ESRS reporters vs. voluntary ESRS reporters, FY2024 | Ambition/DQS score vs. market & risk variables |
| Time horizon | FY2024 (single year, first ESRS wave) | FY2024 (extendable to short panel as data accrues) |
| Treatment / independent variable | Legal obligation to report under ESRS (country transposition status) | Disclosure Quality Score / Climate-Target Ambition Score |
| Unit of analysis | Firm (report-level coding) | Firm–year |
| Causal claim | Quasi-experimental (natural variation in transposition timing) | None — explicitly correlational (see Section 11) |

The longer-run **quasi-experimental longitudinal panel** design described in
earlier drafts of this document (multi-year DiD on disclosure quality and
financial performance, 2015–2024) remains a valid framing for the WP5/WP6
descriptive and estimation work on the broader disclosure-quality panel (RQ2,
RQ4) built from Source B, run in parallel with, not in place of, the Stage 1
ambition study.

---

## 5. Sample Definition

Two distinct samples are used, corresponding to the two data sources
(Section 7). They serve different purposes and are not meant to be merged into
a single firm-year panel except at the scoring/linkage step for Stage 2.

### 5.1 Primary-source acquisition pool (WP2) — Source A

The full report corpus already acquired for the project, functioning as the
coverage pool from which the Stage 1 coding sample is drawn:

- **~1,056 EU-listed/registered companies** with at least one report or ESEF
  package retrieved (per `WORKING_NOTES.md` / `FEHLENDE_BERICHTE_MANUELL.md`,
  status 2026-07-24).
- Materials: PDF annual reports, standalone/integrated sustainability reports,
  ESEF/iXBRL packages, gathered via Bundesanzeiger/Unternehmensregister,
  national OAMs, the Sustainability Reporting Navigator (SRN), and
  company-by-company from investor relations pages where no aggregator had
  complete coverage (see `data/sources/SUSTAINABILITY_REPORT_SOURCES.md`).
- Fiscal-year coverage varies by company; systematic ESEF availability begins
  FY2020, with gaps documented and being closed manually (`FEHLENDE_BERICHTE_MANUELL.md`).
- This pool is a WP2 acquisition asset, not itself the Stage 1 sample; it
  over-represents companies with mature, sustained disclosure practices for
  years extending back before 2020, which is treated as a **scope condition**
  on generalisability, not a bias to correct for.

### 5.2 Stage 1 coding sample — mandatory vs. voluntary comparison

Drawn from the pool in 5.1, restricted to FY2024 reports:

- **Mandatory group**: companies domiciled in EU Member States with completed
  CSRD transposition as of FY2024 reporting.
- **Voluntary group**: companies domiciled in Member States where transposition
  was still pending at FY2024 reporting (incl. Germany), that nonetheless
  reported climate targets in ESRS-aligned structure.
- Sample size and industry balancing to be finalised once the transposition
  tracker (`data/raw/CSRD_Transposition_Tracker.xlsx`) is cross-matched against
  5.1; target is a matched-pairs or stratified design balancing country,
  industry, and firm size across the two groups rather than a large-N panel.

### 5.3 Secondary-source panel — Source B (LSEG Datastream)

Used for Stage 2 (market pricing) and the broader WP5/WP6 disclosure-quality
panel (RQ2/RQ4):

- Companies listed in LSEG Datastream, filtered via Refinitiv/LSEG Navigator
  (status 2026-04-28): Category *Equities*, Market *EU countries + European
  non-EU + EU accession countries*, Type *Equity*, Activity *Active*, Security
  *Major*, Quote *Primary*; no further industry delimitation.
- **Geographical scope**: 27 EU countries, European non-EU countries, EU
  accession countries.
- **Industry scope**: no delimitation at the sampling stage; industry fixed
  effects applied at the estimation stage via ICB sector labels.
- **Temporal scope**: 2015–2025, spanning NFRD entry into force (2017) and
  CSRD entry into force (2024) as the two regulatory interventions.
- Working file: `data/raw/reveald_sample_datastream.csv` (see also the
  Germany- and CSRD-specific extracts in the same folder).

---

## 6. Variables

### Dependent Variables

| Variable | Stage | Operationalisation |
|---|---|---|
| Climate-Target Ambition Score | 1 | Composite score across five criteria (see Section 8.2) |
| Disclosure Quality Score (DQS) | 2 (panel) | Composite scoring model across ESRS dimensions (see Section 8.1) |
| ESRS Coverage Rate | 2 (panel) | Share of mandatory ESRS data points disclosed |
| Double Materiality Completeness | 2 (panel) | Binary/ordinal coding of impact + financial materiality |
| Assurance Status | 2 (panel) | None / limited / reasonable |

### Independent / Treatment Variable (Stage 1)

- Mandatory vs. voluntary ESRS reporting status (binary, derived from
  country-level CSRD transposition status at FY2024 reporting date)

### Key Sustainability Indicators (Outcomes, Stage 1 ambition criteria)

- Reduction pace vs. sector 1.5°C pathway benchmark (SBTi, IEA, or TPI)
- Ambition relative to the firm's own historical emissions trend
- Scope 3 (value-chain) coverage of the stated target
- Presence and proximity of interim milestones vs. distant net-zero only
- Reliance on carbon offsets/compensation; concreteness of stated measures

### Financial / Market Variables (Stage 2, from Source B)

- Market valuation and risk indicators (e.g., market-to-book, ESG-related
  risk/reputational risk measures) — final list to be confirmed pending the
  literature check noted in Section 11
- ROA, ROE, revenue growth
- Leverage, firm size (log total assets)
- Sector and country fixed effects

### Moderators / Mediators

- Firm size (large vs. mid-cap)
- Industry carbon intensity
- Country-level implementation status
- Analyst coverage (proxy for external scrutiny) — Stage 2 only

---

## 7. Data Sources

REVEALD draws on two distinct data sources, each supporting a different
analytical component of the study. The meaningful distinction between them is
not the classical "primary vs. secondary *data*" dichotomy (in that sense,
both are secondary — neither was generated by the REVEALD team for this
study), but **degree of mediation**: Source A is an unmediated primary source
*document*, collected directly from the disclosing entity; Source B is
secondary, compiled/mediated data from a commercial vendor. This terminology
is used consistently to avoid a reviewer objection based on the classical
primary/secondary data convention.

| | Source A | Source B |
|---|---|---|
| **Material** | Annual and sustainability reports, collected directly from company websites / official registers | Firm-level panel data retrieved from LSEG Datastream |
| **Analytical component** | Qualitative content analysis / structured coding | Quantitative panel estimation |
| **Role in design** | Stage 1 ambition scoring; substantive vs. symbolic disclosure assessment | Stage 2 market pricing; DiD/panel estimation of disclosure-quality panel |
| **Classification** | Primary source documents | Secondary (compiled/derived) data |

### 7.1 Source A: Corporate Annual and Sustainability Reports

- **Content**: annual reports and standalone/integrated sustainability reports
  published directly by companies; collected from IR pages, national OAMs
  (e.g. Bundesanzeiger/Unternehmensregister for Germany), and the
  Sustainability Reporting Navigator. See `data/sources/SUSTAINABILITY_REPORT_SOURCES.md`
  for the full list of aggregators checked and why company-by-company
  collection was ultimately required (no single source has complete, current,
  English-language coverage).
- **Purpose**: enables qualitative content analysis distinguishing symbolic
  from substantive transparency (Institutional Theory, Legitimacy Theory
  framing — see `theoretical_framework.md`); provides the textual evidence
  base for Stage 1 ambition coding and for tracing firms' own narrative shifts
  around the NFRD → CSRD/ESRS transition.
- **Methodological classification**: primary source documents in the content-
  analysis sense (cf. Krippendorff) — original, unmediated communications
  produced directly by the entity under study, collected without an
  intervening data vendor. Not "primary data" in the classical sense of
  researcher-generated data (e.g. survey, experiment): the reports were
  produced by companies for stakeholder communication and regulatory
  compliance, not for REVEALD.
- **Known limitations**: longitudinal availability bias (mature disclosers
  over-represented further back in time) is a scope condition, not a
  correctable bias; format heterogeneity (PDF layouts, integrated vs.
  standalone reports) addressed in the extraction/coding protocol
  (`wp2_data_acquisition/coding_manual/`).

### 7.2 Source B: LSEG Datastream

- **Content**: firm-level panel data covering financial variables,
  ESG-related indicators, and ICB sector labels. Working file:
  `data/raw/reveald_sample_datastream.csv`.
- **Purpose**: standardised, comparable panel structure for the Stage 2
  market-pricing analysis and the broader WP5/WP6 disclosure-quality panel;
  supplies outcome and control variables at firm-year level; ICB labels
  support fixed-effects specifications and (pending) mapping to GICS for
  cross-study comparability.
- **Methodological classification**: secondary (compiled/derived) data — a
  commercial vendor extracting, standardising, and redistributing data
  originally disclosed elsewhere, collected for a general commercial purpose,
  not for REVEALD specifically.
- **Known limitations**: vendor coding/standardisation of ESG metrics is not
  fully transparent; restatements/backfilling can affect panel consistency
  (pull-date to be fixed and documented for replication); coverage gaps for
  smaller/non-listed firms limit generalisability beyond large, listed
  companies.

### 7.3 Benchmark sources (Stage 1 ambition assessment)

Free, publicly available sector decarbonisation pathways used to benchmark
stated climate targets (Section 8.2, criterion 1):

- Science Based Targets initiative (SBTi) sector pathways
- International Energy Agency (IEA) sector pathways
- Transition Pathway Initiative (TPI)

### 7.4 Other referenced sources

- Regulatory implementation status: EUR-Lex; national transposition tracker
  (`data/raw/CSRD_Transposition_Tracker.xlsx`, `CSRD_Umsetzung.xlsx`)
- Industry classification: NACE Rev. 2 / ICB / GICS

---

## 8. Disclosure Quality & Climate-Target Ambition Scoring

Two related but distinct scoring instruments are used: the pre-existing
Disclosure Quality Score (DQS), used for the broader panel (RQ2/RQ4, Stage 2
context), and the new Climate-Target Ambition Score, which is the primary
coding instrument for Stage 1.

### 8.1 Disclosure Quality Score (DQS)

The DQS covers five dimensions, each scored on a **0–3 ordinal scale**,
yielding a composite score of **0–15**.

| Dimension | Description | Scale |
|---|---|---|
| 1. Coverage | Share of ESRS topical standards addressed (E1–E5, S1–S4, G1) | 0–3 |
| 2. Granularity | Qualitative vs. quantitative disclosure; presence of metrics and targets | 0–3 |
| 3. Double Materiality | Explicit documentation of impact materiality and financial materiality | 0–3 |
| 4. Forward-looking Orientation | Presence of targets, pathways, scenario analysis | 0–3 |
| 5. Assurance | External verification status and scope | 0–3 |
| **Total DQS** | | **0–15** |

### 8.2 Climate-Target Ambition Score (new, Stage 1)

For each company's FY2024 climate target(s), scored across five criteria
(scale to be finalised during pilot coding, provisionally 0–3 per criterion):

| # | Criterion | Guiding question |
|---|---|---|
| 1 | Pace vs. 1.5°C pathway | How does the stated reduction rate compare to what a recognised sector 1.5°C pathway (SBTi / IEA / TPI) requires? |
| 2 | Ambition vs. own trend | Is the target more ambitious than a simple extrapolation of the firm's own historical emissions trend, or merely a restatement of it? |
| 3 | Value-chain coverage | Does the target cover Scope 3 emissions, where most emissions typically sit, or only Scopes 1–2? |
| 4 | Interim milestones | Are there near-term interim targets, or only a distant net-zero commitment? |
| 5 | Credibility of measures | How reliant is the target on offsets/compensation vs. concrete, named abatement measures? |

Both instruments are documented in full, with anchor examples and decision
rules, in `wp3_reporting_quality/scoring_model.md` and
`wp2_data_acquisition/coding_manual/`.

### 8.3 Intercoder Reliability

Inter-coder reliability is assessed via **Cohen's Kappa** during the pilot
coding phase (20–30 reports for DQS; a comparable pilot batch planned for the
Ambition Score once criterion anchors are finalised).

- Target: **κ ≥ 0.70**
- Disagreements resolved through structured discussion and coding manual
  updates before the main coding phase begins

---

## 9. Analytical Strategy

### Phase 1 — Stage 1 Ambition Analysis (WP3/WP5, primary deliverable)

- Comparative analysis of Climate-Target Ambition Scores between mandatory
  and voluntary ESRS reporters (FY2024), controlling for firm size, industry
  carbon intensity, and country
- Descriptive comparison against 1.5°C sector pathway benchmarks
  (SBTi/IEA/TPI)
- Country and industry breakdowns of ambition and DQS scores

### Phase 2 — Broader Descriptive & Longitudinal Analysis (WP5)

- Time-series plots of DQS and sustainability indicators (2015–2024) from the
  Source B panel
- Structural break tests around NFRD (2018) and CSRD (2024) introduction
- Country and industry heatmaps of reporting maturity

### Phase 3 — Stage 2 Market-Pricing Association (WP6)

Explicitly **correlational, not causal** (see Section 11). Panel regressions
with firm and year fixed effects linking DQS / Ambition Score to market
valuation and risk indicators:

$$Y_{it} = \alpha + \beta_1 \cdot Score_{it} + \gamma X_{it} + \delta_i + \lambda_t + \varepsilon_{it}$$

Where $Y_{it}$ is a market valuation or risk indicator, $Score_{it}$ is the
DQS or Ambition Score, $X_{it}$ are firm-level controls, $\delta_i$/$\lambda_t$
are firm/year fixed effects.

### Phase 4 — Broader Panel DiD (WP6, RQ2/RQ4 context)

Retained from the earlier design as the identification strategy for the
disclosure-quality panel (not for market pricing, which is Phase 3):

$$DQS_{it} = \alpha + \beta_1 \cdot Treated_i + \beta_2 \cdot Post_t + \beta_3 \cdot (Treated_i \times Post_t) + \gamma X_{it} + \delta_i + \lambda_t + \varepsilon_{it}$$

| Symbol | Definition |
|---|---|
| $DQS_{it}$ | Disclosure Quality Score for firm $i$ in year $t$ |
| $Treated_i$ | 1 if firm is subject to CSRD, 0 otherwise |
| $Post_t$ | 1 for years after CSRD entry into force |
| $\beta_3$ | Key treatment effect (DiD estimator) |
| $X_{it}$ | Firm-level control variables |
| $\delta_i$ | Firm fixed effects |
| $\lambda_t$ | Year fixed effects |
| $\varepsilon_{it}$ | Error term |

#### Extensions

- **Staggered DiD** — accounts for variation in CSRD transposition timing
  across countries
- **Event study** — visualises pre-trends and dynamic treatment effects to
  validate the parallel trends assumption for Phase 4 only (not a substitute
  for the abandoned capital-market event study, see Section 2)
- **Robustness checks** — alternative DQS/Ambition weightings, winsorisation
  at 1%/99%, placebo tests, alternative lag structures

#### Software

- **R** (primary): `fixest`, `did`, `tidyverse`
- Replication-ready scripts in `wp6_estimation/scripts/`

---

## 10. Quality Assurance & Research Governance

| Element | Specification |
|---|---|
| Coding manual | Decision rules and anchor examples for DQS and the Ambition Score in `wp2_data_acquisition/coding_manual/` |
| Intercoder reliability | Pilot on 20–30 reports; discrepancies resolved before main coding |
| Data versioning | Timestamped raw data snapshots; documented transformation steps |
| Reproducibility package | Data dictionary, codebook, R scripts, README in `reproducibility_package/` |
| Licensed data | Excluded from version control via `.gitignore`; access instructions in `wp2_data_acquisition/data_governance.md` |

---

## 11. Limitations

| Limitation | Mitigation Strategy |
|---|---|
| Stage 1 sample is single-year (FY2024) and comparatively small | Framed explicitly as first-wave evidence; matched-pairs/stratified design rather than large-N claims |
| No clean capital-market event date exists for CSRD | Original event-study design dropped in favour of the correlational Stage 2 design; not claimed as causal |
| Stage 2 market-pricing results are correlational, not causal | Explicitly labelled as association, not effect, throughout Section 9 Phase 3 and in any publication |
| Self-selection into voluntary ESRS reporting | Matched-pairs design on size/industry/country; robustness tests |
| Benchmark selection (SBTi vs. IEA vs. TPI pathways may disagree) | Report ambition scores under multiple benchmarks as robustness check |
| AI-assisted extraction errors (Source A corpus) | Manual spot-checks on 10% of coded reports |
| Longitudinal availability bias in the Source A corpus | Treated as a scope condition on generalisability, not corrected for |
| Vendor (Datastream) measurement inconsistency | Fix and document pull-date; note vendor methodology gaps |
| Potential greenwashing / symbolic disclosure | Disclosure-ambition gap analysis (DQS vs. Ambition Score) as a robustness check |
| Prior work on market pricing of ESRS-specific quality not yet exhaustively reviewed | Targeted literature check before finalising Stage 2 scope (open item, Section 6 of `REVEALD_Forschungsstand_und_Strategie.md`) |

---

## 12. Target Journals

Given Donau et al. (2025) occupies the top tier for the ESRS first-wave
disclosure-volume result, REVEALD targets well-regarded second-tier
accounting/sustainability journals appropriate for a one-conference,
one-publication project scope:

- Accounting in Europe
- Sustainability Accounting, Management and Policy Journal
- Journal of International Accounting, Auditing and Taxation
- Corporate Social Responsibility and Environmental Management

---

## 13. Timeline

| Month | Work Package | Key Milestone |
|---|---|---|
| 1–2 | WP1 | RQs, hypotheses, sample, variable specification finalised |
| 2–4 | WP2 | Document corpus built; mandatory/voluntary sample matched; panel structure established |
| 3–6 | WP3 | Ambition Score and DQS finalised; pilot + main coding completed |
| 4–7 | WP4 | Financial/sustainability data merged; benchmark pathways integrated; missing-data report |
| 6–8 | WP5 | Stage 1 comparative analysis; descriptive panel analyses; structural break tests |
| 7–10 | WP6 | Stage 2 market-pricing association; broader panel DiD; robustness checks |
| 10–12 | WP7 | Conference paper submitted; reproducibility package delivered |

---

## References

> See `docs/bibliography/reveald.bib` for the full BibTeX reference list.

Key references for this research design:

- Donau, C., Sellhorn, T. et al. (2025). Targeting Transparency: Early
  Evidence on Mandatory Adoption of European Sustainability Reporting
  Standards. *Working paper.*
- Grewal, J., Riedl, E.J., & Serafeim, G. Market reaction to mandatory
  non-financial disclosure regulation (NFRD capital-market event study).
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
