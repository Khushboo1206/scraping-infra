from flask import Flask, jsonify
from database.postgres import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Books Scraper API Running",
        "endpoints": [
            "/books",
            "/count",
            "/search/<keyword>"
        ]
    })


@app.route("/books")
def get_books():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, price
        FROM products
        LIMIT 20
    """)

    books = cursor.fetchall()

    result = []

    for title, price in books:
        result.append({
            "title": title,
            "price": price
        })

    cursor.close()
    conn.close()

    return jsonify(result)


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


@app.route("/search/<keyword>")
def search_books(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT title, price
        FROM products
        WHERE title ILIKE %s
        LIMIT 20
        """,
        (f"%{keyword}%",)
    )

    books = cursor.fetchall()

    result = []

    for title, price in books:
        result.append({
            "title": title,
            "price": price
        })

    cursor.close()
    conn.close()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)