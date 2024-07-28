# Book Recommendation System with FastAPI and Milvus

### Youtube Video Link: https://youtu.be/dvb2NSbkq1s

## Project Overview

This project is a book recommendation system that leverages FastAPI for the API, Milvus for vector similarity search, and Sentence Transformers for generating embeddings from book descriptions. The system allows users to query for book recommendations based on a given search term and returns a list of relevant books along with various performance metrics.

## Project Structure

```
book-bot-fastapi-metrics/
├── app.py
├── book_data.py
├── book_data.json
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

```
Python 3.8+
Docker
Google Books API Key
```

## Setup and Installation

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/book-bot-fastapi-metrics.git
cd book-bot-fastapi-metrics
```

### 2. Install Dependencies

It is recommended to use a virtual environment to manage dependencies.

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory and add your Google Books API key.

```
GOOGLE_BOOKS_API_KEY=your_google_books_api_key
```

### 4. Fetch Book Data

Run the `book_data.py` script to fetch book data from the Google Books API.

```sh
python book_data.py
```

This will create a `book_data.json` file with book information and their embeddings.

### 5. Run Milvus with Docker

Ensure Docker is running on your system. Use the provided `docker-compose.yml` to start Milvus.

```sh
docker-compose up -d
```

### 6. Start the FastAPI Server

Run the `main.py` script to start the FastAPI server.

```sh
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

## Usage

### API Endpoints

- **GET /**: Health check endpoint.
- **POST /books/**: Get book recommendations.

#### Example Request

```sh
curl -X POST "http://127.0.0.1:8000/books/" -H "Content-Type: application/json" -d "{\"query\": \"science books\"}"
```

### Response

The API returns a JSON response with a list of recommended books and performance metrics.

```json
{
  "books": [
    {
      "title": "The Science Book",
      "authors": "DK",
      "description": "A comprehensive guide to key topics in science.",
      "published_date": "2015-02-02",
      "categories": "Science",
      "average_rating": "N/A",
      "ratings_count": "N/A",
      "thumbnail": "http://books.google.com/books/content?id=Z4eKBgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
      "preview_link": "http://books.google.ca/books?id=Z4eKBgAAQBAJ&printsec=frontcover&dq=science&hl=&cd=1&source=gbs_api"
    }
  ],
  "metrics": {
    "Context Precision": 0.0,
    "Context Recall": 0.0,
    "Context Relevance": 0.027085579723616533,
    "Context Entity Recall": 0.0,
    "Noise Robustness": 0.0,
    "Faithfulness": 0.0,
    "Answer Relevance": 0.027085579723616533,
    "Information Integration": 0.0,
    "Counterfactual Robustness": 0.0,
    "Negative Rejection": 0.0,
    "Latency": 0.9891576766967773
  }
}
```

## Project Components

### `book_data.py`

This script fetches book data from the Google Books API based on predefined queries and stores the data in `book_data.json`.

### `main.py`

This is the main FastAPI application. It initializes the sentence transformer model, encodes book descriptions into embeddings, and sets up the API endpoints.

### `app.py`

This script contains the application logic for fetching book data and handling API requests.

### `requirements.txt`

Contains all the Python dependencies required for the project.

## Contributing

Contributions are welcome! Please create an issue or pull request for any feature requests, bug fixes, or enhancements.

## License

This project is licensed under the MIT License.

---
