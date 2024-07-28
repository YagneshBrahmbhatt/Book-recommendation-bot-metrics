import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import json
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

try:
    embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    logger.info("Successfully initialized embeddings.")
except Exception as e:
    logger.error(f"Error initializing embeddings: {e}")
    raise

json_file_path = 'book_data.json'
with open(json_file_path, 'r') as file:
    book_data = json.load(file)

for book in book_data:
    text_to_embed = f"{book['description']} [CATEGORY: {book['categories']}]"
    book['embedding'] = embeddings.encode([text_to_embed])[0]

class UserQuery(BaseModel):
    query: str

@app.post("/books/")
async def get_books(user_query: UserQuery):
    try:
        logger.info(f"Received query: {user_query.query}")

        query_embedding = embeddings.encode([user_query.query])[0]

        similarities = []
        for book in book_data:
            similarity = query_embedding @ book['embedding']
            similarities.append((similarity, book))

        similarities.sort(reverse=True, key=lambda x: x[0])

        recommendations = []
        for _, book in similarities[:5]:
            book_copy = book.copy()
            del book_copy['embedding']
            recommendations.append(book_copy)

        return {"books": recommendations}
    except Exception as e:
        logger.error(f"Error during book retrieval: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
