# Web Sources That Collect Corporate/Sustainability Reports

Overview of websites and registers that aggregate corporate annual, CSR, and sustainability
reports across multiple companies. Created as a supplement to this project's own research
(see `WORKING_NOTES.md`, `FEHLENDE_BERICHTE_MANUELL.md`), where reports were ultimately
sourced company-by-company from official websites, since none of the sources below offer
complete, current, English-language coverage on their own.

---

## General Aggregators for Annual/CSR Reports

| Source | Description | Link |
|---|---|---|
| **AnnualReports.com** | Large free library of annual reports (PDF) for many global companies, often including integrated ESG/sustainability sections. Coverage is not exhaustive and the most recent year isn't always available. | https://www.annualreports.com |
| **ResponsibilityReports.com** | Sister site to AnnualReports.com, specialized in CSR/sustainability reports by company/industry. Free, with decent historical archives. | https://www.responsibilityreports.com |
| **Report Watch** (Radley Yeldar) | Aggregates annual reports mainly for large European/FTSE companies, sometimes with design/benchmarking commentary. | https://www.reportwatch.net |
| **WBCSD Reporting Exchange** | Curated database of sustainability/ESG reports and disclosure requirements; more framework/policy-oriented than a complete PDF archive. | https://www.reportingexchange.com |

## CSRD-Specific Indexes

| Source | Description | Link |
|---|---|---|
| **Sustainability Reporting Navigator (SR Navigator)** | Continuously updated index specifically for English-language CSRD sustainability reports of European companies, fiscal years 2024 onward (~1,837 reports as of research). Filterable by country/sector/industry/year, with comparison and AI-query tools. Free, optional login. Indexes/links to reports rather than hosting the PDFs itself, and is limited to 2024+ fiscal years — not useful for the 2017–2023 history this project needed. | https://srnav.com/reports |

## Standards-Body Registries (Voluntary Self-Registration)

| Source | Description | Link |
|---|---|---|
| **GRI Sustainability Disclosure Database** | Reports that companies have self-registered as GRI-aligned. Coverage depends on voluntary registration and is therefore incomplete. | https://database.globalreporting.org |
| **CDP** | Climate/water/forest disclosure responses (questionnaire-based), not full sustainability reports, but often linked from them. | https://www.cdp.net |

## Regulatory Filing Registers (Authoritative for EU ESRS/CSRD Reports)

| Source | Description | Link |
|---|---|---|
| **filings.xbrl.org** | Aggregates ESEF/iXBRL filings from EU "Officially Appointed Mechanisms" (OAMs). Patchy coverage — e.g. almost no German issuers are indexed even though the filings exist. | https://filings.xbrl.org |
| **Bundesanzeiger / Unternehmensregister** | German company register; official source for ESEF packages of German issuers. Access is mostly interactive (session/JS portal), no deep-linking via curl. | https://www.unternehmensregister.de |
| **FCA National Storage Mechanism** | Central UK repository for regulated company announcements, including UKSEF/iXBRL annual reports of British issuers. | https://data.fca.org.uk |
| **ESAP – European Single Access Point** | EU-wide central access point being built by ESMA for company filings (including sustainability reports), intended to unify the fragmented OAM landscape. Still in rollout — not yet a full substitute for national registers. | https://esap.esma.europa.eu |
| **SEC EDGAR Full-Text Search** | Full-text search over US mandatory filings (e.g. 10-K) including climate/ESG-related disclosures of US issuers. | https://www.sec.gov/cgi-bin/browse-edgar |

---

**Bottom line:** None of these sources reliably cover all ~750+ companies needed for this
project with complete, current, English-language PDF links. That's why reports were
ultimately sourced company-by-company directly from each official investor relations page
(see `WORKING_NOTES.md`).
