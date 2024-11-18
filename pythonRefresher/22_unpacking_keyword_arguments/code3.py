# Creates a dictionary from inputted arguments:
def named(**kwargs):
    # Prints the whole dictionary:
    print(kwargs)

def print_nicely(**kwargs):
    # Runs the above function with the key / value pairs input.
    # Output is a dictionary.
    named(**kwargs)

    # Prints formatted keys and values:
    # kwargs = a dictionary    
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_nicely(name="Bob", age=25)

