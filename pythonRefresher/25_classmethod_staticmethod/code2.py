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

print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

# If we used 'book' without __repr__ we'd get a weird object printout.
# So we have to be spcific and print out only the book name.
print(book.name)

# Uses __repr__:
print(book)

