# Factory using classmethod. You can create new objects (instantiate the class)
# within the class itself.

class Book:
    # Class variables become class properties:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    # __repr__ allows us to customize a representation of the Book class.
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight {self.weight}g.>"
    
    @classmethod
    def hardcover(cls, name, weight):
        # Creates a new object inside the class:
        return Book(name, Book.TYPES[0], weight)
    
    @classmethod
    def paperpack(cls, name, weight):
        return Book(name, Book.TYPES[1], weight)

# Don't need to create a new object due to the classmethod:
book = Book.hardcover("Harry Potter", 1500)
print(book)

book2 = Book.paperpack("Fairytale", 1600)
print(book2)

