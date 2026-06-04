import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="scraping_db",
        user="postgres",
        password="postgres9767",
        port="5432"
    )

    return conn