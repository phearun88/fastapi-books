# 📚 Book Management API (FastAPI)

A professional FastAPI project for managing books, built using a clean and scalable architecture. This project demonstrates best practices such as layered structure, Pydantic models, and modular routing.

---

## 🚀 Features

* Get all books
* Filter books by category or author
* Get a single book by title
* Create a new book
* Update an existing book
* Delete a book
* Clean architecture (Router → Service → Data)
* Input validation using Pydantic
* Ready for scaling with database integration

---

## 📂 Project Structure

```
fastapi-books/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── books.py
│   ├── models/
│   │   └── book_models.py
│   ├── services/
│   │   └── book_service.py
│   └── data/
│       └── book_data.py
│
├── tests/
│   └── test_books.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-project.git
cd book-project
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open your browser:

* API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 📌 API Endpoints

### Get all books

```
GET /books/
```

### Filter books

```
GET /books/?category=science
GET /books/?author=Author One
GET /books/?author=Author One&category=math
```

### Get book by title

```
GET /books/{book_title}
```

### Create a book

```
POST /books/
```

Request body:

```json
{
  "title": "New Book",
  "author": "John Doe",
  "category": "technology"
}
```

### Update a book

```
PUT /books/
```

Request body:

```json
{
  "id": 1,
  "title": "Updated Title",
  "author": "Updated Author",
  "category": "science"
}
```

### Delete a book

```
DELETE /books/{book_id}
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🧠 Technologies Used

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic
* Pytest

---

## 📈 Future Improvements

* Add database (PostgreSQL, MySQL)
* Use SQLAlchemy or Prisma ORM
* Add authentication (JWT)
* Add pagination and sorting
* Deploy using Docker and AWS

---

## 👨‍💻 Author

**Phearun Phin**

* Full Stack .NET & Python Developer
* Interested in AI Engineering and Microservices

---

## 📄 License

This project is open-source and available for learning and personal use.

---

## ⭐ Notes

This project is designed for learning and portfolio purposes. It follows clean architecture principles and can be extended into a production-ready system.
