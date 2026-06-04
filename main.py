from scrapers.books_scraper import scrape_books
from database.operations import insert_book

total_books = 0

for page in range(1, 6):

    books = scrape_books(page)

    for book in books:

        insert_book(
            book["title"],
            book["price"]
        )

        total_books += 1

print(f"\nInserted {total_books} books into PostgreSQL")