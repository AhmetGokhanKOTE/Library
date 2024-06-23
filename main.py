from book import Book
from patron import Patron
from librarian import Librarian
from library import Library

library = Library("Politechnika Library")

book1 = Book("Araba Sevdası", "Recaizade Mahmud Ekrem", "001")
book2 = Book("Animal Farm", "George Orwell", "002")

librarian = Librarian("Ahmet Kote", "L1")

patron1 = Patron("Gokhan Kote", "P1")
patron2 = Patron("", "")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)

patron1.borrow_book(book1)
book1.available = True

print(" Books in the library:")
print(library.list_books())
 
print("\n Patrons in the library:")
print(library.list_patrons())

patron1.return_book(book1)
book1.available = False

print("\n Books in the library after returning a book:")
print(library.list_books())

