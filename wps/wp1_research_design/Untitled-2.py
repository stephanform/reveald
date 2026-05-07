"""
SIC Code Crawler – siccode.com
==============================
Crawlt alle 4-stelligen SIC-Codes von https://siccode.com/
und speichert sie als CSV mit zwei Spalten:
  - sic_code : 4-stelliger SIC-Code (z. B. 3699)
  - sic_name : Klartext-Bezeichnung

Benötigt: pip install requests beautifulsoup4
Aufruf:   python sic_crawler.py
Ausgabe:  sic_codes.csv
"""

import csv
import time
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://siccode.com"
OUTPUT_FILE = "sic_codes.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 (research script)"}
PAUSE = 0.5  # Sekunden zwischen Requests


def get(url: str) -> BeautifulSoup:
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def main():
    results = []

    # Schritt 1: Alle 2-stelligen Major-Group-Links von der Startseite holen
    print("Lade Startseite ...")
    soup = get(BASE_URL + "/sic-codes-list")

    major_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Links wie /sic-codes-list/XX oder /sic-code/XX
        if re.match(r"^/sic-codes?(-list)?/\d{2}$", href):
            url = BASE_URL + href
            if url not in [m["url"] for m in major_links]:
                major_links.append({"url": url, "text": a.get_text(strip=True)})

    print(f"  → {len(major_links)} Major Groups gefunden")

    # Schritt 2: Jede Major Group aufrufen und 4-stellige SIC-Codes extrahieren
    for i, mg in enumerate(major_links, 1):
        print(f"[{i}/{len(major_links)}] {mg['url']}")
        time.sleep(PAUSE)
        try:
            mg_soup = get(mg["url"])
            for a in mg_soup.find_all("a", href=True):
                href = a["href"]
                # 4-stellige SIC-Codes: /sic-code/XXXX
                m = re.match(r"^/sic-code/(\d{4})$", href)
                if m:
                    code = m.group(1)
                    name = a.get_text(strip=True)
                    if name and {"sic_code": code} not in [{"sic_code": r["sic_code"]} for r in results]:
                        results.append({"sic_code": code, "sic_name": name})
        except Exception as e:
            print(f"  FEHLER: {e}")

    # Schritt 3: Sortieren und als CSV speichern
    results.sort(key=lambda x: x["sic_code"])
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["sic_code", "sic_name"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✓ Fertig! {len(results)} SIC-Codes gespeichert in '{OUTPUT_FILE}'")
    print("\nVorschau (erste 5 Einträge):")
    for r in results[:5]:
        print(f"  {r['sic_code']}  {r['sic_name']}")


if __name__ == "__main__":
    main()