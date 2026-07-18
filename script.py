import json
import os


class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued,
            "issued_to": self.issued_to
        }

    @staticmethod
    def from_dict(data):
        book = Book(data["isbn"], data["title"], data["author"])
        book.is_issued = data["is_issued"]
        book.issued_to = data["issued_to"]
        return book

    def __str__(self):
        status = f"Issued to {self.issued_to}" if self.is_issued else "Available"
        return f"[{self.isbn}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self, filepath="library_data.json"):
        self.filepath = filepath
        self.books = {}
        self.load_data()

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = Book(isbn, title, author)
        self.save_data()
        print(f"Added: {title}")

    def remove_book(self, isbn):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        removed = self.books.pop(isbn)
        self.save_data()
        print(f"Removed: {removed.title}")

    def search_by_title(self, keyword):
        keyword = keyword.lower()
        return [book for book in self.books.values() if keyword in book.title.lower()]

    def search_by_author(self, keyword):
        keyword = keyword.lower()
        return [book for book in self.books.values() if keyword in book.author.lower()]

    def issue_book(self, isbn, member_name):
        book = self.books.get(isbn)
        if not book:
            print(f"No book found with ISBN {isbn}.")
            return
        if book.is_issued:
            print(f"'{book.title}' is already issued to {book.issued_to}.")
            return
        book.is_issued = True
        book.issued_to = member_name
        self.save_data()
        print(f"Issued '{book.title}' to {member_name}.")

    def return_book(self, isbn):
        book = self.books.get(isbn)
        if not book:
            print(f"No book found with ISBN {isbn}.")
            return
        if not book.is_issued:
            print(f"'{book.title}' was not issued.")
            return
        book.is_issued = False
        book.issued_to = None
        self.save_data()
        print(f"Returned '{book.title}'.")

    def total_books(self):
        return len(self.books)

    def issued_count(self):
        return sum(1 for book in self.books.values() if book.is_issued)

    def available_count(self):
        return self.total_books() - self.issued_count()

    def generate_report(self):
        print("----- Library Report -----")
        print(f"Total books: {self.total_books()}")
        print(f"Issued: {self.issued_count()}")
        print(f"Available: {self.available_count()}")
        print("---------------------------")

    def list_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books.values():
            print(book)

    def save_data(self):
        with open(self.filepath, "w") as f:
            data = [book.to_dict() for book in self.books.values()]
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return
            for entry in data:
                book = Book.from_dict(entry)
                self.books[book.isbn] = book


def print_menu():
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Search by Title")
    print("4. Search by Author")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. List All Books")
    print("8. Generate Report")
    print("9. Exit")


def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            isbn = input("Enter ISBN: ").strip()
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            library.add_book(isbn, title, author)

        elif choice == "2":
            isbn = input("Enter ISBN to remove: ").strip()
            library.remove_book(isbn)

        elif choice == "3":
            keyword = input("Enter title keyword: ").strip()
            results = library.search_by_title(keyword)
            if results:
                for book in results:
                    print(book)
            else:
                print("No matches found.")

        elif choice == "4":
            keyword = input("Enter author keyword: ").strip()
            results = library.search_by_author(keyword)
            if results:
                for book in results:
                    print(book)
            else:
                print("No matches found.")

        elif choice == "5":
            isbn = input("Enter ISBN to issue: ").strip()
            member = input("Enter member name: ").strip()
            library.issue_book(isbn, member)
            print(f"Total books: {library.total_books()}, Issued: {library.issued_count()}, Available: {library.available_count()}")

        elif choice == "6":
            isbn = input("Enter ISBN to return: ").strip()
            library.return_book(isbn)

        elif choice == "7":
            library.list_all_books()

        elif choice == "8":
            library.generate_report()

        elif choice == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()