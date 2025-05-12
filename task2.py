from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging
from typing import Protocol

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


@dataclass
class Book:
    title: str
    author: str
    year: str


class LibraryInterface(Protocol):
    def add_book(self, book: Book) -> None: ...
    def remove_book(self, title: str) -> None: ...
    def list_books(self) -> list[Book]: ...


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [b for b in self._books if b.title != title]

    def list_books(self) -> list[Book]:
        return self._books.copy()


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logging.info("Book added successfully")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logging.info("Book removed successfully")

    def show_books(self) -> None:
        books = self.library.list_books()
        if not books:
            logging.info("No books available")
        for book in books:
            logging.info(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()
        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

