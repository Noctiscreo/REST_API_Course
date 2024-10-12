# # Get input from user as a STRING:
# name = input("Enter your name: ")
# print("Your name is " + name)

# Get input from user, convert STRING to INT:
size_input = input("How big is your house (in square feet)?: ")
square_feet = int(size_input)
square_metres = square_feet / 10.8

# Use an 'f string' to combine int and str.
# Use :.2f to round up 2 decimal places in the float:
print(f"{square_feet} sq feet is: {square_metres} sq metres.")

