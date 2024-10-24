# Don't do this (make a parameter = a default variable)

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)

# Because, if we change the default variable, this does not modify the function:
default_y = 4

#So the below has the same result, which is '5':
add(2)

