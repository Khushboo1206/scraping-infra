from scrapers.books_scraper import scrape_books

all_books = []

for page in range(1, 4):

    books = scrape_books(page)

    all_books.extend(books)

print(f"Total books: {len(all_books)}")