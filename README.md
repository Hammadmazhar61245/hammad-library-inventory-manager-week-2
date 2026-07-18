# Library Book Inventory Manager

A simple command-line library management system built in Python. Supports adding, removing, searching, issuing, and returning books, with data persisted to a JSON file so nothing is lost between runs.

## Features

- Add and remove books from the inventory
- Search books by title or author (partial, case-insensitive match)
- Issue books to members and mark them returned
- View all books with their current status
- Generate a report showing total, issued, and available book counts
- Automatic JSON persistence — data is saved after every change and reloaded on startup

## Project Structure

- `Book` — represents a single book (isbn, title, author, issue status, issued-to member)
- `Library` — manages the collection of books using a dictionary keyed by ISBN for fast lookup, and handles JSON read/write
- `main()` — command-line menu that drives the program

## Requirements

- Python 3.6+
- No external dependencies (uses only the standard library: `json`, `os`)

## How to Run

```bash
python3 library_manager.py
```

On first run, a `library_data.json` file will be created in the same directory to store your book data. On subsequent runs, existing data is loaded automatically.

## Menu Options

1. **Add Book** — enter ISBN, title, and author
2. **Remove Book** — remove a book by ISBN
3. **Search by Title** — find books matching a keyword in the title
4. **Search by Author** — find books matching a keyword in the author name
5. **Issue Book** — mark a book as issued to a member
6. **Return Book** — mark an issued book as returned
7. **List All Books** — display every book and its status
8. **Generate Report** — show total, issued, and available book counts
9. **Exit** — quit the program

## Data Storage

Books are stored in `library_data.json` as a list of objects:

```json
[
    {
        "isbn": "1234",
        "title": "Atomic Habits",
        "author": "James Clear",
        "is_issued": true,
        "issued_to": "Hammad"
    }
]
```

## Notes

- ISBN is used as the unique identifier for each book, so it must be unique when adding new entries.
- If a book's ISBN is not found during search, issue, or return operations, the program will notify you instead of crashing.
