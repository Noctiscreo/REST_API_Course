# Unpack the dictionary keys and values.
def named(name, age):
    print(name, age)

details_1 = {"name": "Bob", "age": 25}

named(**details_1)


# Output the whole dictionary:
def named_kwargs(**kwargs):
    print(kwargs)

details_2 = {"name": "Bob", "age": 25}

named_kwargs(**details_2)

