from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book_by_title():
    response = client.get("/books/Title One")
    assert response.status_code == 200
    assert response.json()["title"] == "Title One"


def test_create_book():
    new_book = {
        "title": "New Book",
        "author": "New Author",
        "category": "technology"
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201
    assert response.json()["title"] == "New Book"