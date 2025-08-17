
class Book:
    def __init__(self, title: str, author: str):
        """Base class representing a book"""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Derived class representing an eBook"""
        super().__init__(title, author)  # Call parent constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Derived class representing a printed book"""
        super().__init__(title, author)  # Call parent constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Class demonstrating composition with a collection of books"""
        self.books = []

    def add_book(self, book: Book):
        """Add a book (Book, EBook, or PrintBook) to the library"""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            print(book)
