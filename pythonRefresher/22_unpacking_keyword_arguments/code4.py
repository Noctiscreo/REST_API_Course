# Combination of both *args and **kwargs.

def both(*args, **kwargs):
    print(args)
    print(kwargs)

# *args can be unlimited in number:
both(1, 3, 5, name="Bob", age=25)

