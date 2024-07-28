import os
import requests
import json
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

google_books_api_key = os.getenv("GOOGLE_BOOKS_API_KEY")
if not google_books_api_key:
    raise ValueError("Please set the GOOGLE_BOOKS_API_KEY environment variable.")

def fetch_book_data(google_books_api_key, query, max_results=40):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={google_books_api_key}&maxResults={max_results}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        raise Exception(f"Failed to fetch data from Google Books: {response.status_code}")

book_data = []
queries = ["fiction", "nonfiction", "mystery", "fantasy", "science", "history"]

for query in queries:
    books = fetch_book_data(google_books_api_key, query)
    for book in books:
        volume_info = book['volumeInfo']
        book_entry = {
            "title": volume_info.get('title', 'N/A'),
            "authors": ", ".join(volume_info.get('authors', 'N/A')),
            "description": volume_info.get('description', 'N/A'),
            "published_date": volume_info.get('publishedDate', 'N/A'),
            "categories": ", ".join(volume_info.get('categories', 'N/A')),
            "average_rating": volume_info.get('averageRating', 'N/A'),
            "ratings_count": volume_info.get('ratingsCount', 'N/A'),
            "thumbnail": volume_info.get('imageLinks', {}).get('thumbnail', 'N/A'),
            "preview_link": volume_info.get('previewLink', 'N/A')
        }
        book_data.append(book_entry)
        if len(book_data) >= 1000:
            break
    if len(book_data) >= 1000:
        break
    time.sleep(0.5)

with open('book_data.json', 'w') as f:
    json.dump(book_data, f, indent=4)

print(f"Total books retrieved: {len(book_data)}")
