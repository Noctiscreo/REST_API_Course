class ClassTest:
    # An instance of the class is needed to call an instance method.
    # When 'self' is the object of a class, it is an instance method. 
    # Instance methods are the most widely used.
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # Class methods used often as 'factories.'
    # Class methods do not need an instance of the class.
    # The 'cls' parameter is the class itself.
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # Static methods don't take any class info or objects.
    # Static methods are purely for organizational use. They don't need
    # a class to be insantiated. Rarely used.
    @staticmethod
    def static_method():
        print("Called static_method.")

    
#Instantiate the class:
test = ClassTest()

# Call the instance_method method 1:
test.instance_method()

# Call the instance_method method 2:
ClassTest.instance_method(test)

# Call the class_method. You DO NOT need an instance of the class:
# **Note that python knows to input (ClassTest) by default.
ClassTest.class_method()

# Call the static_method:
ClassTest.static_method()

