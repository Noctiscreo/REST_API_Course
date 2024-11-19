class Person:
    # MAGIC METHODS are called automatically by Python in certin conditions.
    # e.g. '__init__' is called by Python when instantiating a class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # The __str__ MAGIC METHOD turns your object into a string:
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."
    
    # The __str__ method will be printed out by default. 
    # Comment it out to see the below.
    # __repr__ is used by programmers to print 'unambiguous objects'.
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
    

bob = Person("Bob", 35)

# Prints the 'bob' object that changes when you use __str__.
print(bob)

