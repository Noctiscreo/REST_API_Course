
class Student():
    # A function inside a class is called a 'method'.
    # The init method is automatically called.
    def __init__(self, name, grades):
        # self.name = this instance variable.
        # '= name' is taken from the argument when the class is instantiated.
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Rolf", (100, 100, 93, 78, 90))
student2 = Student("Bob", (90, 90, 93, 78, 90))

print(student1.name)
print(student1.average())

print(student2.name)
print(student2.average())

