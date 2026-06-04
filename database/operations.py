from database.postgres import get_connection

def insert_book(title, price):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO products(title, price)
        VALUES (%s, %s)
        """,
        (title, price)
    )

    conn.commit()

    cursor.close()

    conn.close()