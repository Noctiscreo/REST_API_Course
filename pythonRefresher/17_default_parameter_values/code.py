# cannot have a default parameter followed by a non-default parameter:
def add(x=5, y):
    print(x + y)

# cannot put a positional argument after a keyword or named argument:
add(x=5, 5)

