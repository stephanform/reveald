"""
SIC Code Lookup Table Generator
================================
Lädt alle SIC-Codes von der offiziellen OSHA-Website
(https://www.osha.gov/data/sic-manual) und speichert
sie als CSV-Datei.

Ausgabe: sic_codes.csv
Spalten:
  - sic_code      : 4-stelliger SIC-Code (z. B. 3699)
  - division      : Übergeordnete Division (z. B. "D")
  - division_name : Name der Division (z. B. "Manufacturing")
  - major_group   : 2-stellige Hauptgruppe (z. B. 36)
  - major_group_name : Name der Hauptgruppe
  - industry_group: 3-stellige Industriegruppe (z. B. 369)
  - sic_name      : Bezeichnung des SIC-Codes im Klartext

Benötigt: requests, beautifulsoup4
Installation: pip install requests beautifulsoup4
"""

import csv
import re
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.osha.gov"
SIC_MANUAL_URL = f"{BASE_URL}/data/sic-manual"
OUTPUT_FILE = "sic_codes.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 (research script)"}


def get_soup(url: str, retries: int = 3) -> BeautifulSoup:
    """HTTP-GET mit Retry-Logik, gibt BeautifulSoup-Objekt zurück."""
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"  Fehler (Versuch {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                time.sleep(2)
    raise RuntimeError(f"Konnte URL nicht laden: {url}")


def parse_division_links(soup: BeautifulSoup) -> list[dict]:
    """Extrahiert alle Division-Links von der SIC-Hauptseite."""
    divisions = []
    # OSHA listet die Divisionen als Links auf der Hauptseite
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "/data/sic-manual/division" in href:
            divisions.append({
                "url": BASE_URL + href if href.startswith("/") else href,
                "name": link.get_text(strip=True)
            })
    return divisions


def parse_major_group_links(soup: BeautifulSoup, base_url: str) -> list[dict]:
    """Extrahiert Major-Group-Links von einer Division-Seite."""
    groups = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "/data/sic-manual/major-group" in href:
            groups.append({
                "url": BASE_URL + href if href.startswith("/") else href,
                "name": link.get_text(strip=True)
            })
    return groups


def parse_sic_codes_from_major_group(soup: BeautifulSoup) -> list[dict]:
    """
    Extrahiert 4-stellige SIC-Codes und ihre Bezeichnungen
    von einer Major-Group-Seite.
    """
    codes = []
    # SIC-Codes erscheinen typischerweise als Links oder in Tabellen
    for link in soup.find_all("a", href=True):
        href = link["href"]
        # SIC-Codes haben URLs wie /data/sic-manual/sic-code-XXXX
        match = re.search(r"sic-code[/-](\d{4})", href)
        if match:
            code = match.group(1)
            name = link.get_text(strip=True)
            if name and code:
                codes.append({"sic_code": code, "sic_name": name})
    return codes


def extract_header_info(soup: BeautifulSoup) -> dict:
    """Extrahiert Division- und Major-Group-Info aus dem Seiten-Header."""
    info = {
        "division": "",
        "division_name": "",
        "major_group": "",
        "major_group_name": "",
        "industry_group": ""
    }
    # Versuche h1/h2 auszulesen
    for tag in ["h1", "h2"]:
        heading = soup.find(tag)
        if heading:
            text = heading.get_text(strip=True)
            # Major Group z. B. "Major Group 36: Electronic Equipment"
            mg_match = re.search(r"Major Group\s+(\d{2})[:\-]\s*(.+)", text, re.I)
            if mg_match:
                info["major_group"] = mg_match.group(1)
                info["major_group_name"] = mg_match.group(2).strip()
            # Division z. B. "Division D: Manufacturing"
            div_match = re.search(r"Division\s+([A-Z])[:\-]\s*(.+)", text, re.I)
            if div_match:
                info["division"] = div_match.group(1)
                info["division_name"] = div_match.group(2).strip()
    return info


def derive_industry_group(sic_code: str) -> str:
    """Leitet die 3-stellige Industriegruppe aus dem 4-stelligen SIC ab."""
    return sic_code[:3] if len(sic_code) == 4 else ""


def main():
    print("=" * 60)
    print("SIC Code Lookup Table Generator")
    print("Quelle: OSHA SIC Manual (https://www.osha.gov/data/sic-manual)")
    print("=" * 60)

    all_records = []

    # 1. Hauptseite laden
    print("\n[1/3] Lade SIC-Hauptseite ...")
    main_soup = get_soup(SIC_MANUAL_URL)
    divisions = parse_division_links(main_soup)
    print(f"  → {len(divisions)} Divisionen gefunden")

    # 2. Jede Division durchlaufen
    print("\n[2/3] Durchlaufe Divisionen und Major Groups ...")
    for div in divisions:
        print(f"\n  Division: {div['name']}")
        div_soup = get_soup(div["url"])
        major_groups = parse_major_group_links(div_soup, div["url"])
        print(f"    → {len(major_groups)} Major Groups")

        for mg in major_groups:
            time.sleep(0.3)  # höfliche Pause zwischen Requests
            try:
                mg_soup = get_soup(mg["url"])
                header = extract_header_info(mg_soup)
                sic_codes = parse_sic_codes_from_major_group(mg_soup)

                # Falls Division-Info nicht auf MG-Seite: von Division übernehmen
                if not header["division"]:
                    div_match = re.search(r"Division\s+([A-Z])", div["name"], re.I)
                    if div_match:
                        header["division"] = div_match.group(1)
                    header["division_name"] = div["name"]

                for sc in sic_codes:
                    all_records.append({
                        "sic_code": sc["sic_code"],
                        "division": header["division"],
                        "division_name": header["division_name"],
                        "major_group": header["major_group"],
                        "major_group_name": header["major_group_name"],
                        "industry_group": derive_industry_group(sc["sic_code"]),
                        "sic_name": sc["sic_name"]
                    })

                print(f"      {header['major_group']} – {len(sic_codes)} Codes geladen")
            except Exception as e:
                print(f"      FEHLER bei {mg['url']}: {e}")

    # 3. CSV speichern
    print(f"\n[3/3] Speichere {len(all_records)} Einträge in '{OUTPUT_FILE}' ...")
    fieldnames = [
        "sic_code", "division", "division_name",
        "major_group", "major_group_name",
        "industry_group", "sic_name"
    ]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_records)

    print(f"\n✓ Fertig! Datei gespeichert: {OUTPUT_FILE}")
    print(f"  Gesamtzahl SIC-Codes: {len(all_records)}")

    # Kurze Vorschau
    print("\nVorschau (erste 5 Einträge):")
    print("-" * 80)
    for rec in all_records[:5]:
        print(f"  {rec['sic_code']} | {rec['major_group_name'][:30]:<30} | {rec['sic_name']}")
    print("-" * 80)


if __name__ == "__main__":
    main()