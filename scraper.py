import csv
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

START_URL = "https://books.toscrape.com/"
MAX_PAGES = 5  # change to None to scrape all 50 pages


def scrape_page(url):
    """Download one page and return its books plus the link to the next page."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()   # stop with a clear error if the page fails to load
    response.encoding = "utf-8"   # fixes the £ sign showing as Â£

    soup = BeautifulSoup(response.text, "html.parser")

    rows = []
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rows.append([title, price])

    next_link = soup.select_one("li.next a")
    next_url = urljoin(url, next_link["href"]) if next_link else None
    return rows, next_url


def main():
    url = START_URL
    all_rows = []
    pages = 0

    while url and (MAX_PAGES is None or pages < MAX_PAGES):
        try:
            rows, url = scrape_page(url)
        except requests.RequestException as error:
            print(f"Could not load {url}: {error}")
            break
        all_rows.extend(rows)
        pages += 1
        print(f"Page {pages}: {len(rows)} books")

    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])
        writer.writerows(all_rows)

    print(f"Done! Saved {len(all_rows)} books to books.csv")


if __name__ == "__main__":
    main()
