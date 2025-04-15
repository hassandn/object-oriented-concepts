# represents a relationship where one class contains a reference to another class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)        

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author        


library = Library("City Library")

bool1 = Book("meow book","jfk")
book2 = Book("dog book","jfadk")
book3 = Book("cat book","jfsaffk")

library.add_book(bool1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())