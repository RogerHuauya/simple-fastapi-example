# FastAPI Books CRUD App

This is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI, SQLite, and Jinja2 for templating. The app allows users to manage a collection of books through a web interface.

## Features

- **Create**: Add a new book with a title and author.
- **Read**: View a list of all books.
- **Update**: Edit the details of a book.
- **Delete**: Remove a book from the list.

## Requirements

- Python 3.9 or higher
- Virtual environment setup (optional, but recommended)

## Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/fastapi-books-crud.git
cd fastapi-books-crud
```

### 2. Create and activate a virtual environment

Using `venv`:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install the dependencies

After activating the virtual environment, install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

Once all dependencies are installed, you can start the FastAPI application using Uvicorn.

```bash
uvicorn app:app --reload
```

The `--reload` option will automatically reload the server if you make changes to your code.

### 5. Access the Web Interface

Open your web browser and go to:

```
http://127.0.0.1:8000
```

This is where you can interact with the web interface to add, edit, and delete books.

### 6. API Documentation

FastAPI provides automatic API documentation at:

```
http://127.0.0.1:8000/docs
```

Here, you can test the API endpoints directly using the interactive Swagger UI.

## Folder Structure

```
fastapi-crud
│
├── app.py               # Main FastAPI app
├── templates            # Folder containing Jinja2 HTML templates
│   ├── index.html       # HTML for listing books
│   └── edit.html        # HTML for editing a book
├── requirements.txt     # Python dependencies
└── README.md            # This readme file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or pull requests if you find any bugs or have suggestions for improvements.
