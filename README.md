
---
# REVEAL'D
**Regulatory Evaluation of ESG-Aligned Disclosure**

Bremen University of Applied Sciences (HSB) · Faculty Fk1 (Business)
 · DTX Cluster Project · Project Lead: Prof. Dr. Stephan Form · ORCID: 0009-0008-1396-4323

---

## Project Description
REVEALD examines the implementation and effectiveness of corporate
sustainability reporting regulation in the EU (NFRD → CSRD/ESRS). Its
primary deliverable is a comparative study of climate-target ambition in
the first mandatory wave of ESRS reports (FY2024): are targets more
ambitious and credible under legal obligation than under voluntary
adoption (natural variation from delayed national CSRD transposition,
incl. Germany)? A second, correlational stage then asks whether capital
markets price disclosure quality and target ambition differently.

**Methodology:** mixed-methods, staged design —
(1) qualitative content analysis and structured scoring (Disclosure
Quality Score, Climate-Target Ambition Score) of primary reports,
comparing mandatory vs. voluntary ESRS reporters; followed by
(2) quantitative panel analysis linking those scores to market/risk
indicators (correlational, not causal — no clean capital-market event
date exists for CSRD). See `docs/research_design/research_design_by_claude.md`
for full design and positioning against related work (Donau et al. 2025).

**Data sources:** two distinct sources, kept methodologically separate —
**Source A**, primary source documents (annual/sustainability reports,
ESEF filings collected directly from companies and national registers,
~1,000+ EU companies acquired, FY2024 sub-sample coded for the ambition
comparison), used for the qualitative component; and **Source B**,
LSEG Datastream, a secondary/vendor-compiled panel of financial and ESG
indicators, used for the quantitative component. See
`wps/wp2_data_acquisition/data_sources.md` and
`data/sources/SUSTAINABILITY_REPORT_SOURCES.md`.

---

## Repository Structure

| Folder                      | Content                                                       |
| --------------------------- | ------------------------------------------------------------- |
| `docs/`                     | Proposal, research design, meeting minutes, bibliography      |
| `wps/`                      | Working Packages                                              |
| `wps/wp1_research_design/`  | Research questions, sample definition, variable specification |
| `wps/wp2_data_acquisition/` | Data sources, governance, coding manual, report corpus index  |
| `wps/wp3_reporting_quality/`| DQS scoring model, intercoder protocol, coding results        |
| `wps/wp4_indicators/`       | Sustainability & financial indicators, harmonisation rules    |
| `wps/wp5_descriptive/`      | Figures, tables, structural break notes                       |
| `wps/wp6_estimation/`       | Modelling strategy, R scripts (DiD, event study, robustness)  |
| `wps/wp7_publications/`     | Conference materials, journal paper drafts                    |
| `data/`                     | Raw and processed data (see note below)                       |
| `reproducibility_package/`  | Final replication materials for journal submission            |

---

## Data Note
Raw and processed data files are excluded from version control
(`.gitignore`): Source B (LSEG Datastream) due to licensing restrictions,
Source A (company reports) to limit repository size. Access/retrieval
instructions are documented in `wp2_data_acquisition/data_governance.md`
and `wp2_data_acquisition/data_sources.md`.

---

## Project Timeline

| Phase | Months |
|---|---|
| WP1 – Research design | 1–2 |
| WP2 – Data acquisition | 2–4 |
| WP3 – Coding | 3–6 |
| WP4 – Indicator integration | 4–7 |
| WP5 – Descriptive analysis | 6–8 |
| WP6 – Estimation | 7–10 |
| WP7 – Publications | 10–12 |

---

## How to Clone
```bash
git clone https://github.com/stephanform/reveald.git
```

## License
See `LICENSE` for details.
"# reveald" 
