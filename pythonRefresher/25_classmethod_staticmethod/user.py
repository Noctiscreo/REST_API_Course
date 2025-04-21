class User:
    def __init__(self, first_name, last_name, age, ethnicity, occupation): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ethnicity = ethnicity
        self.occupation = occupation
    
    def describe_user(self):
        print(f"User Name: {self.first_name} {self.last_name}\nAge: {self.age}\nEthnicity: {self.ethnicity}\nOccupation: {self.occupation}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
        

user1 = User("Bob", "Smith", 24, "White", "Plumber")
user2 = User("Fred", "Bloggs", 27, "Black", "Lawyer")
user3 = User("Mary", "Bishop", 33, "Asian", "Soldier")
user4 = User("Sally", "Perkins", 45, "Hispanic", "Teacher")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()