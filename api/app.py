from flask import Flask, jsonify, request
from database.postgres import get_connection
import os

print("DB_HOST =", os.getenv("DB_HOST"))
app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Scraping Infrastructure API is running"
    })


@app.route("/count")
def count_books():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM products"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({
        "total_books": count
    })


@app.route("/books")
def get_books():

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    offset = (page - 1) * limit

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, price
        FROM products
        ORDER BY id
        LIMIT %s OFFSET %s
        """,
        (limit, offset)
    )

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    result = []

    for book in books:
        result.append({
            "id": book[0],
            "title": book[1],
            "price": str(book[2])
        })

    return jsonify(result)


@app.route("/quotes")
def get_quotes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, quote, author
        FROM quotes
        ORDER BY id
        LIMIT 20
        """
    )

    quotes = cursor.fetchall()

    cursor.close()
    conn.close()

    result = []

    for quote in quotes:
        result.append({
            "id": quote[0],
            "quote": quote[1],
            "author": quote[2]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )