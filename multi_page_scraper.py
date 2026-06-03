import requests
import pandas as pd
from bs4 import BeautifulSoup

data = []

for page in range(1, 4):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        data.append({
            "title": title,
            "price": price,
            "page": page
        })

df = pd.DataFrame(data)

df.to_csv("all_books.csv", index=False)

print(f"Saved {len(data)} books")