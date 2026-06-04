from database.postgres import get_connection


def insert_quote(
    quote,
    author
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO quotes(
            quote,
            author
        )
        VALUES (%s,%s)
        """,
        (
            quote,
            author
        )
    )

    conn.commit()

    cursor.close()

    conn.close()