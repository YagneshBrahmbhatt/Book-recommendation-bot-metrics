import streamlit as st
import requests

st.title("Book Recommendation Chatbot")

BASE_URL = "http://localhost:8000"

query = st.text_input("Ask anything about books")

if st.button("Get Recommendation"):
    try:
        response = requests.post(f"{BASE_URL}/books/", json={"query": query})
        response.raise_for_status()

        if response.status_code == 200:
            response_json = response.json()
            books = response_json.get("books")

            st.write("Books:")
            for book in books:
                st.write(f"**Title:** {book['title']}")
                st.write(f"**Authors:** {book['authors']}")
                st.write(f"**Description:** {book['description']}")
                st.write(f"**Published Date:** {book['published_date']}")
                st.write(f"**Categories:** {book['categories']}")
                st.write(f"**Average Rating:** {book['average_rating']}")
                st.write(f"**Ratings Count:** {book['ratings_count']}")
                st.image(book['thumbnail'])
                st.write(f"**Preview Link:** [Read More]({book['preview_link']})")
                st.write("-" * 40)
        else:
            st.error("Failed to fetch books. Please try again.")
    except requests.exceptions.RequestException as e:
        st.error("Unable to connect to the book recommendation service. Please try again later.")
    except Exception as e:
        st.error("An unexpected error occurred. Please try again later.")
