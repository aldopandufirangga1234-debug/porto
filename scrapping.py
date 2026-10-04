"""
Mini Project Day 7: Async Web Scraper
Scraping beberapa URL sekaligus (paralel) pakai asyncio + aiohttp,
lalu simpan hasilnya ke CSV.

Install dulu:
    pip install aiohttp beautifulsoup4
"""

import asyncio
import csv
import aiohttp
from bs4 import BeautifulSoup

# 1. Daftar URL yang mau di-scrape (ganti sesuai kebutuhan)
URLS = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
    "https://quotes.toscrape.com/page/3/",
]


async def fetch_html(session: aiohttp.ClientSession, url: str) -> str:
    """Ambil HTML dari satu URL."""
    async with session.get(url) as response:
        return await response.text()


def parse_quotes(html: str) -> list[dict]:
    """Parsing HTML jadi data yang kita mau (judul quote + author)."""
    soup = BeautifulSoup(html, "html.parser")
    data = []
    for quote_div in soup.select(".quote"):
        text = quote_div.select_one(".text").get_text(strip=True)
        author = quote_div.select_one(".author").get_text(strip=True)
        data.append({"quote": text, "author": author})
    return data


async def scrape_one(session: aiohttp.ClientSession, url: str) -> list[dict]:
    """Gabungan fetch + parse untuk satu URL."""
    html = await fetch_html(session, url)
    return parse_quotes(html)


async def scrape_all(urls: list[str]) -> list[dict]:
    """Jalankan scraping semua URL SECARA PARALEL pakai asyncio.gather."""
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_one(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    # gabungkan semua list jadi satu
    all_data = []
    for result in results:
        all_data.extend(result)
    return all_data


def save_to_csv(data: list[dict], filename: str = "quotes.csv"):
    """Simpan hasil scraping ke file CSV."""
    if not data:
        print("Tidak ada data untuk disimpan.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Tersimpan {len(data)} data ke {filename}")


async def main():
    print(f"Mulai scraping {len(URLS)} halaman secara paralel...")
    data = await scrape_all(URLS)
    save_to_csv(data)


if __name__ == "__main__":
    asyncio.run(main())