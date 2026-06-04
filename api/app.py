from flask import Flask, jsonify, request
from database.postgres import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Books Scraper API Running",
        "endpoints": [
            "/books?page=1&limit=20",
            "/books/<id>",
            "/count",
            "/search/<keyword>"
        ]
    })


@app.route("/books")
def get_books():

    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 20, type=int)

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

    result = []

    for book_id, title, price in books:
        result.append({
            "id": book_id,
            "title": title,
            "price": price
        })

    cursor.close()
    conn.close()

    return jsonify({
        "page": page,
        "limit": limit,
        "results": result
    })


@app.route("/books/<int:book_id>")
def get_book(book_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, price
        FROM products
        WHERE id = %s
        """,
        (book_id,)
    )

    book = cursor.fetchone()

    cursor.close()
    conn.close()

    if not book:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify({
        "id": book[0],
        "title": book[1],
        "price": book[2]
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


@app.route("/search/<keyword>")
def search_books(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, price
        FROM products
        WHERE title ILIKE %s
        LIMIT 20
        """,
        (f"%{keyword}%",)
    )

    books = cursor.fetchall()

    result = []

    for book_id, title, price in books:
        result.append({
            "id": book_id,
            "title": title,
            "price": price
        })

    cursor.close()
    conn.close()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)