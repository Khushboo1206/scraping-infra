from scrapers.quotes_scraper import scrape_quotes
from database.quote_operations import insert_quote

quotes = scrape_quotes()

for quote in quotes:

    insert_quote(
        quote["quote"],
        quote["author"]
    )

print(
    f"Inserted {len(quotes)} quotes"
)