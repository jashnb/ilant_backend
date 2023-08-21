from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/api/search-books")
async def search_books(query: str, page: int = 1, items_per_page: int = 10):
    google_books_api_url = "https://www.googleapis.com/books/v1/volumes"

    offset = (page - 1) * items_per_page

    params = {"q": query, "startIndex": offset, "maxResults": items_per_page}

    async with httpx.AsyncClient() as client:
        print("making API call")
        response = await client.get(google_books_api_url, params=params)
        print(f"Api call done: {response}")
        response_data = response.json()
        print(response_data)
        # Process the response and extract relevant book information
        books = []
        print(response_data.get("totalItems"))
        print(len(response_data.get("items", [])))
        for item in response_data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            book = {
                "id": item.get("id"),
                "title": volume_info.get("title"),
                "authors": ", ".join(volume_info.get("authors", [])),
                "description": volume_info.get("description"),
                "coverUrl": volume_info.get("imageLinks", {}).get("thumbnail"),
            }
            books.append(book)
        print(len(books))
        return {"books": books}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
