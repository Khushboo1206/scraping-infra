# Scraping Infrastructure Platform

A Python-based data scraping and API platform that collects data from multiple websites, stores it in PostgreSQL, and exposes the data through REST APIs built with Flask.

---

## Features

* Multi-source web scraping
* PostgreSQL database integration
* REST API using Flask
* Pagination support
* Search-ready architecture
* Dockerized deployment
* Environment variable configuration
* Logging and error handling
* Retry mechanism for failed requests

---

## Tech Stack

### Backend

* Python
* Flask

### Web Scraping

* BeautifulSoup4
* Requests

### Database

* PostgreSQL
* Psycopg2

### DevOps

* Docker
* Docker Compose

### Utilities

* Python Dotenv
* Logging

---

## Project Structure

```text
scraping-infra/
│
├── api/
│   └── app.py
│
├── database/
│   ├── postgres.py
│   ├── operations.py
│   └── quote_operations.py
│
├── scrapers/
│   ├── books_scraper.py
│   ├── quotes_scraper.py
│   └── logger.py
│
├── main.py
├── quotes_main.py
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Data Sources

### Books To Scrape

https://books.toscrape.com

Collected Data:

* Book Title
* Book Price

### Quotes To Scrape

https://quotes.toscrape.com

Collected Data:

* Quote
* Author

---

## Database Schema

### Products Table

| Column | Type               |
| ------ | ------------------ |
| id     | SERIAL PRIMARY KEY |
| title  | TEXT               |
| price  | TEXT               |

### Quotes Table

| Column | Type               |
| ------ | ------------------ |
| id     | SERIAL PRIMARY KEY |
| quote  | TEXT               |
| author | TEXT               |

---

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Scraping Infrastructure API is running"
}
```

---

### Get Total Books Count

```http
GET /count
```

Response:

```json
{
  "total_books": 200
}
```

---

### Get Books

```http
GET /books?page=1&limit=5
```

Response:

```json
[
  {
    "id": 1,
    "title": "A Light in the Attic",
    "price": "£51.77"
  }
]
```

---

### Get Quotes

```http
GET /quotes
```

Response:

```json
[
  {
    "id": 1,
    "quote": "The world as we have created it...",
    "author": "Albert Einstein"
  }
]
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/scraping-infra.git
cd scraping-infra
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_NAME=scraping_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

---

## Running Scrapers

### Books Scraper

```bash
python main.py
```

### Quotes Scraper

```bash
python quotes_main.py
```

---

## Running API

```bash
python -m api.app
```

API available at:

```text
http://127.0.0.1:5000
```

---

## Docker Setup

Build and start services:

```bash
docker compose up --build
```

Stop services:

```bash
docker compose down
```

---

## Future Improvements

* Search APIs
* Scheduled scraping
* Data export to CSV
* Authentication
* API documentation using Swagger
* Cloud deployment

---

## Learning Outcomes

This project demonstrates:

* Web Scraping
* Backend Development
* REST API Design
* PostgreSQL Integration
* Docker Containerization
* Error Handling
* Logging
* Environment Management
* Software Project Structure

---

## Author

Khushboo Nimje

GitHub:
https://github.com/Khushboo1206
