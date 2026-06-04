import requests
from bs4 import BeautifulSoup
from scrapers.logger import logger
import time


def scrape_books(page):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        )
    }

    max_retries = 3

    for attempt in range(max_retries):

        try:

            logger.info(f"Scraping page {page}")

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            books = soup.find_all(
                "article",
                class_="product_pod"
            )

            data = []

            for book in books:

                title = book.h3.a["title"]

                price = book.find(
                    "p",
                    class_="price_color"
                ).text

                data.append({
                    "title": title,
                    "price": price
                })

            logger.info(
                f"Found {len(data)} books on page {page}"
            )

            return data

        except requests.exceptions.RequestException as e:

            logger.error(
                f"Attempt {attempt + 1} failed: {e}"
            )

            time.sleep(2)

    logger.error(
        f"Failed to scrape page {page}"
    )

    return []