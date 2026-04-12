"""
================================================================
REVEALD – Repository Structure Setup Script (Python version)
================================================================
This script creates the full folder and placeholder file
structure for the REVEALD research project repository.

HOW TO RUN:
  1. Place this file in the folder where you want the repo
     to be created (or in an already cloned GitHub repo folder)
  2. Open a terminal / command prompt in that folder
  3. Run:  python setup_reveald_repo.py

REQUIREMENTS:
  - Python 3.6 or higher (no external packages needed)

THINGS YOU MAY WANT TO EDIT BEFORE RUNNING:
  - Line 40  : GITHUB_USERNAME  → your GitHub username
  - Line 41  : REPO_NAME        → your repository name on GitHub
  - Line 42  : AUTHOR_NAME      → project lead name for README
  - Line 43  : AUTHOR_ORCID     → project lead ORCID for README
================================================================
"""

import os
import textwrap

# ================================================================
# ✏️  EDIT THESE FOUR LINES BEFORE RUNNING
# ================================================================
GITHUB_USERNAME = "stephanform"        # e.g. "stephanform"
REPO_NAME       = "reveald"                     # e.g. "reveald"
AUTHOR_NAME     = "Prof. Dr. Stephan Form"      # project lead
AUTHOR_ORCID    = "0009-0008-1396-4323"         # ORCID iD
# ================================================================


def make(path):
    """Create a directory (including parents) if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def touch(path, content=""):
    """Create a file with optional content; never overwrites existing files."""
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def create_structure():

    print("Creating REVEALD repository structure...\n")

    # ── .gitignore ───────────────────────────────────────────
    touch(".gitignore", textwrap.dedent("""\
        # R
        .Rhistory
        .RData
        .Rproj.user/
        *.Rproj

        # Data (licensed/sensitive – do not commit)
        data/raw/
        data/processed/

        # Python
        __pycache__/
        *.pyc
        .env

        # OS
        .DS_Store
        Thumbs.db

        # Temp
        *.tmp
        *.log
    """))

    # ── LICENSE (placeholder) ────────────────────────────────
    touch("LICENSE", "Add your chosen license text here.\n")

    # ── README.md ────────────────────────────────────────────
    touch("README.md", textwrap.dedent(f"""\
        # REVEALD
        **Regulatory Evaluation of ESG-Aligned Disclosure**

        Bremen University of Applied Sciences (HSB) · Faculty Fk1 (Business)
        Project Lead: {AUTHOR_NAME} · ORCID: {AUTHOR_ORCID}

        ---

        ## Project Description
        REVEALD examines the implementation and effectiveness of corporate
        sustainability reporting regulation in the EU (NFRD → CSRD/ESRS),
        using a quasi-experimental longitudinal panel design. It analyses
        disclosure quality and sustainability indicator development across a
        treatment group (CSRD-compliant reporters) and a control group,
        enabling causal inference on the effects of regulatory change.

        ---

        ## Repository Structure

        | Folder | Content |
        |---|---|
        | `docs/` | Proposal, research design, meeting minutes, bibliography |
        | `wp1_research_design/` | Research questions, sample definition, variable specification |
        | `wp2_data_acquisition/` | Data sources, governance, coding manual, report corpus index |
        | `wp3_reporting_quality/` | DQS scoring model, intercoder protocol, coding results |
        | `wp4_indicators/` | Sustainability & financial indicators, harmonisation rules |
        | `wp5_descriptive/` | Figures, tables, structural break notes |
        | `wp6_estimation/` | Modelling strategy, R scripts (DiD, event study, robustness) |
        | `wp7_publications/` | Conference materials, journal paper drafts |
        | `data/` | Raw and processed data (see note below) |
        | `reproducibility_package/` | Final replication materials for journal submission |

        ---

        ## Data Note
        Raw and processed data files are excluded from version control
        (`.gitignore`) due to licensing restrictions (Refinitiv, Bloomberg,
        etc.). Access instructions are documented in
        `wp2_data_acquisition/data_governance.md`.

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
        git clone https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git
        ```

        ## License
        See `LICENSE` for details.
    """))

    # ── docs/ ────────────────────────────────────────────────
    for folder in [
        "docs/proposal",
        "docs/research_design",
        "docs/meetings",
        "docs/bibliography",
    ]:
        make(folder)
        touch(f"{folder}/.gitkeep")

    touch("docs/bibliography/reveald.bib",
          "% BibTeX reference file for REVEALD\n% Add references here\n")

    # ── wp1_research_design/ ─────────────────────────────────
    make("wp1_research_design")
    touch("wp1_research_design/research_questions.md",
          "# Research Questions & Hypotheses\n\n## RQ1 (Dynamics)\n\n## RQ2 (Tensions)\n\n## RQ3 (Comparative)\n\n## Hypotheses\n")
    touch("wp1_research_design/sample_definition.md",
          "# Sample Definition\n\n## Geographical Scope\n\n## Industry Scope\n\n## Index / Universe\n")
    touch("wp1_research_design/variable_specification.md",
          "# Variable Specification\n\n## Dependent Variables\n\n## Independent Variables\n\n## Control Variables\n\n## Moderators / Mediators\n")

    # ── wp2_data_acquisition/ ────────────────────────────────
    make("wp2_data_acquisition/coding_manual")
    make("wp2_data_acquisition/report_corpus")
    touch("wp2_data_acquisition/data_sources.md",
          "# Data Sources\n\n## Sustainability / Annual Reports\n\n## ESG Data Providers\n\n## Financial Indicators\n\n## Regulatory & Classification Sources\n")
    touch("wp2_data_acquisition/data_governance.md",
          "# Data Governance\n\n## Versioning Rules\n\n## Reproducibility Protocol\n\n## Access Instructions for Licensed Data\n")
    touch("wp2_data_acquisition/coding_manual/coding_manual_v01.md",
          "# Coding Manual v0.1 (Draft)\n\n## Purpose\n\n## ESRS Coverage Dimensions\n\n## Scoring Rules\n\n## Decision Rules & Anchor Examples\n")
    touch("wp2_data_acquisition/coding_manual/coding_manual_final.md",
          "# Coding Manual (Final)\n")
    touch("wp2_data_acquisition/report_corpus/corpus_index.csv",
          "firm_id,isin,company_name,country,industry_nace,year,report_type,report_url,download_date,notes\n")

    # ── wp3_reporting_quality/ ───────────────────────────────
    make("wp3_reporting_quality/pilot_coding")
    make("wp3_reporting_quality/main_coding")
    touch("wp3_reporting_quality/scoring_model.md",
          "# Disclosure Quality Scoring Model (DQS)\n\n## Dimensions\n1. Coverage\n2. Granularity\n3. Double Materiality\n4. Forward-looking Orientation\n5. Assurance\n\n## Scale (0–3 per dimension, composite 0–15)\n\n## Anchor Examples\n")
    touch("wp3_reporting_quality/intercoder_protocol.md",
          "# Intercoder Reliability Protocol\n\n## Procedure\n\n## Pilot Phase (20–30 reports)\n\n## Kappa Target: κ ≥ 0.70\n\n## Conflict Resolution Rules\n")
    touch("wp3_reporting_quality/pilot_coding/.gitkeep")
    touch("wp3_reporting_quality/main_coding/.gitkeep")

    # ── wp4_indicators/ ──────────────────────────────────────
    make("wp4_indicators")
    touch("wp4_indicators/indicator_selection.md",
          "# Indicator Selection\n\n## Sustainability Indicators\n- Emissions intensity (Scope 1+2)\n- Energy intensity\n- Target pathway disclosure\n\n## Financial / Performance Indicators\n- ROA, ROE\n- Revenue growth\n- Leverage, firm size\n")
    touch("wp4_indicators/harmonisation_rules.md",
          "# Harmonisation Rules\n\n## Currency Conversion\n\n## Unit Standardisation\n\n## Winsorisation (1% / 99%)\n\n## Identifier Mapping (ISIN / LEI / Mnemonics)\n")
    touch("wp4_indicators/missing_data_report.md",
          "# Missing Data Report\n\n## Overview of Gaps\n\n## Treatment Decisions\n\n## Imputation / Exclusion Rules\n")

    # ── wp5_descriptive/ ─────────────────────────────────────
    make("wp5_descriptive/figures")
    make("wp5_descriptive/tables")
    touch("wp5_descriptive/figures/.gitkeep")
    touch("wp5_descriptive/tables/.gitkeep")
    touch("wp5_descriptive/structural_break_notes.md",
          "# Structural Break Analysis Notes\n\n## NFRD Introduction (2017/2018)\n\n## CSRD Transition (2024)\n\n## Observed Patterns\n")

    # ── wp6_estimation/ ──────────────────────────────────────
    make("wp6_estimation/scripts")
    touch("wp6_estimation/modelling_strategy.md",
          "# Modelling Strategy\n\n## DiD Specification\n\n## Panel Fixed Effects\n\n## Event Study Design\n\n## Robustness Tests\n\n## Moderation & Mediation (Tensions)\n")

    r_scripts = {
        "00_setup.R":             "# 00_setup.R\n# Load packages and set global options\n\nlibrary(tidyverse)\nlibrary(fixest)\nlibrary(did)\n",
        "01_data_import.R":       "# 01_data_import.R\n# Import raw data from data/raw/\n",
        "02_cleaning.R":          "# 02_cleaning.R\n# Data cleaning and variable construction\n",
        "03_panel_construction.R":"# 03_panel_construction.R\n# Build firm-year panel structure\n",
        "04_descriptives.R":      "# 04_descriptives.R\n# Descriptive statistics and exploratory plots\n",
        "05_did_main.R":          "# 05_did_main.R\n# Main DiD estimation\n# DQS_it = alpha + beta1*Treated + beta2*Post + beta3*(Treated x Post) + controls + FE\n",
        "06_event_study.R":       "# 06_event_study.R\n# Event study: pre-trends and dynamic treatment effects\n",
        "07_robustness.R":        "# 07_robustness.R\n# Robustness checks: alternative DQS weights, placebo tests, lag structures\n",
        "08_moderation.R":        "# 08_moderation.R\n# Tensions hypothesis: interaction DQS x financial performance\n",
    }
    for filename, content in r_scripts.items():
        touch(f"wp6_estimation/scripts/{filename}", content)

    # ── wp7_publications/ ────────────────────────────────────
    make("wp7_publications/conference")
    make("wp7_publications/journal_paper/figures")
    touch("wp7_publications/conference/.gitkeep")
    touch("wp7_publications/journal_paper/paper_v01.md",
          "# REVEALD – Working Paper v0.1\n\n## Abstract\n\n## 1. Introduction\n\n## 2. Institutional Background\n\n## 3. Data & Methodology\n\n## 4. Results\n\n## 5. Discussion\n\n## 6. Conclusion\n\n## References\n")
    touch("wp7_publications/journal_paper/figures/.gitkeep")

    # ── data/ ────────────────────────────────────────────────
    make("data/raw")
    make("data/processed")
    touch("data/raw/.gitkeep")
    touch("data/processed/.gitkeep")
    touch("data/codebook.md",
          "# Data Codebook\n\n## Variable Definitions\n\n| Variable | Description | Unit | Source |\n|---|---|---|---|\n")

    # ── reproducibility_package/ ─────────────────────────────
    make("reproducibility_package/scripts")
    touch("reproducibility_package/README_repro.md",
          "# Reproducibility Package\n\n## Step-by-step Replication Instructions\n\n### 1. Data Access\n\n### 2. Software Requirements\n\n### 3. Script Execution Order\n\n### 4. Expected Outputs\n")
    touch("reproducibility_package/data_dictionary.md",
          "# Data Dictionary\n")
    touch("reproducibility_package/codebook.md",
          "# Codebook\n")
    touch("reproducibility_package/scripts/.gitkeep")

    # ── Summary ──────────────────────────────────────────────
    print("✓ Repository structure created successfully!\n")
    print("Next steps:")
    print("  1. git init                                  (if not already a repo)")
    print("  2. git add .")
    print('  3. git commit -m "Initial repository structure"')
    print(f"  4. git remote add origin https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git")
    print("  5. git push -u origin main\n")


if __name__ == "__main__":
    create_structure()