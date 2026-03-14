from app.data.book_data import BOOKS
from app.models.book_models import BookCreate, BookUpdate


def get_all_books():
    return BOOKS


def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book
    return None


def get_books_by_category(category: str):
    return [
        book for book in BOOKS
        if book["category"].casefold() == category.casefold()
    ]


def get_books_by_author(author: str):
    return [
        book for book in BOOKS
        if book["author"].casefold() == author.casefold()
    ]


def get_books_by_author_and_category(author: str, category: str):
    return [
        book for book in BOOKS
        if book["author"].casefold() == author.casefold()
        and book["category"].casefold() == category.casefold()
    ]


def create_book(book: BookCreate):
    new_id = max(book_item["id"] for book_item in BOOKS) + 1 if BOOKS else 1
    new_book = {"id": new_id, **book.model_dump()}
    BOOKS.append(new_book)
    return new_book


def update_book(book: BookUpdate):
    for index, existing_book in enumerate(BOOKS):
        if existing_book["id"] == book.id:
            BOOKS[index] = book.model_dump()
            return BOOKS[index]
    return None


def delete_book(book_id: int):
    for index, book in enumerate(BOOKS):
        if book["id"] == book_id:
            deleted_book = BOOKS.pop(index)
            return deleted_book
    return None