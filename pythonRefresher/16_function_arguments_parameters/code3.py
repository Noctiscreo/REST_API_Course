def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool! You can't divide by zero.")

# Not all arguments have to be keyword arguments:
divide(15, divisor=0)

# However the below code is illegal.
# You can't have a keyword argument before a positional argument:
# divide(dividend=15, 0)

# Tip: Use keyword arguments when things get more complicated
# to make things easier to read.