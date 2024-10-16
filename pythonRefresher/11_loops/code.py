grades = [35, 67, 98, 100, 100]
total = 0

# How many grades in the list? 5
amount = len(grades)

# Add all the grades together.
for grade in grades:
    total = total + grade
average = total / amount
print(average)
