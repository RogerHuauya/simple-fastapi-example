import os
from fastapi import FastAPI, Request, Depends, HTTPException, Form
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# PostgreSQL Database configuration from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create the PostgreSQL engine
engine = create_engine(DATABASE_URL)

# Create a session maker for PostgreSQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for book
class BookCreate(BaseModel):
    title: str
    author: str

# FastAPI app and templates setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Home page - list books
@app.get("/", response_class=HTMLResponse)
def read_books(request: Request, db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return templates.TemplateResponse("index.html", {"request": request, "books": books})

# Create a new book
@app.post("/create", response_class=RedirectResponse)
def create_book(title: str = Form(...), author: str = Form(...), db: Session = Depends(get_db)):
    db_book = Book(title=title, author=author)
    db.add(db_book)
    db.commit()
    return RedirectResponse("/", status_code=303)

# Edit a book form
@app.get("/edit/{book_id}", response_class=HTMLResponse)
def edit_book(book_id: int, request: Request, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return templates.TemplateResponse("edit.html", {"request": request, "book": book})

# Update a book
@app.post("/update/{book_id}", response_class=RedirectResponse)
def update_book(book_id: int, title: str = Form(...), author: str = Form(...), db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = title
    book.author = author
    db.commit()
    return RedirectResponse("/", status_code=303)

# Delete a book
@app.get("/delete/{book_id}", response_class=RedirectResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return RedirectResponse("/", status_code=303)