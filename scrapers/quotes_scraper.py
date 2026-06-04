import requests
from bs4 import BeautifulSoup
from scrapers.logger import logger


def scrape_quotes():

    logger.info("Scraping quotes")

    url = "https://quotes.toscrape.com"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    quotes = soup.find_all(
        "div",
        class_="quote"
    )

    data = []

    for quote in quotes:

        text = quote.find(
            "span",
            class_="text"
        ).text

        author = quote.find(
            "small",
            class_="author"
        ).text

        data.append({
            "quote": text,
            "author": author
        })

    return data