# Book Scraper

A Python web scraper that collects book titles and prices from [books.toscrape.com](https://books.toscrape.com), a website built for scraping practice, and saves them to a CSV file.

## What it does

1. Downloads a page of the book catalogue with **Requests**
2. Reads the HTML with **BeautifulSoup** and finds each book's title and price
3. Follows the **Next** link to move through multiple pages
4. Saves everything to `books.csv`, which opens like a spreadsheet

It also stops with a clear message if a page fails to load, and handles the £ sign correctly.

## Built with

- Python 3
- Requests
- BeautifulSoup (bs4)
- csv (Python standard library)

## Run it

```bash
pip install -r requirements.txt
python3 scraper.py
```

By default it scrapes 5 pages (100 books). Set `MAX_PAGES = None` in `scraper.py` to scrape all 50 pages.

## Sample output

| Title | Price |
| --- | --- |
| A Light in the Attic | £51.77 |
| Tipping the Velvet | £53.74 |
| Soumission | £50.10 |

## Ideas for next steps

- Collect more details per book (rating, stock status)
- Run automatically on a schedule
- Save to a database instead of CSV

## Author

Saheed Muhammed: [sababuilds.vercel.app](https://sababuilds.vercel.app)
