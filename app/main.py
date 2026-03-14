from fastapi import FastAPI
from app.routers import books

app = FastAPI(
    title="Book Management API",
    description="A professional FastAPI project structure for managing books",
    version="1.0.0"
)

app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Book Management API"}