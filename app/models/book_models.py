from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=50)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    id: int


class BookResponse(BookBase):
    id: int