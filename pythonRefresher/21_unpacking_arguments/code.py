# You can define an unspecified number of arguments in a function.
# 'args' is the variable name for the arguments.
# * creates a tuple of the arguments when the function gets called:
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    
    return total

print(multiply(1, 3, 5, 2))

