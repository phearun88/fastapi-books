from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from app.models.book_models import BookCreate, BookResponse, BookUpdate
from app.services.book_service import (
    get_all_books,
    get_book_by_title,
    get_books_by_category,
    get_books_by_author,
    get_books_by_author_and_category,
    create_book,
    update_book,
    delete_book,
)

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[BookResponse])
async def read_books(
    category: Optional[str] = Query(default=None),
    author: Optional[str] = Query(default=None)
):
    if author and category:
        return get_books_by_author_and_category(author, category)
    if author:
        return get_books_by_author(author)
    if category:
        return get_books_by_category(category)
    return get_all_books()

@router.get("/{book_title}", response_model=BookResponse)
async def read_book(book_title: str):
    book = get_book_by_title(book_title)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=BookResponse, status_code=201)
async def add_book(book: BookCreate):
    return create_book(book)


@router.put("/", response_model=BookResponse)
async def edit_book(book: BookUpdate):
    updated = update_book(book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@router.delete("/{book_id}")
async def remove_book(book_id: int):
    deleted = delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully", "book": deleted}