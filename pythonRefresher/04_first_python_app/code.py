# Print a user's age in seconds:
user_age = int(input("Enter your age: "))
months = user_age * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# OR:
easy_seconds = user_age * 31556952

print(f"Your age is {user_age}, which is equal to {months} months.")
print(f"You have been alive for at least {seconds:,} seconds.")
print(f"Easy version: {easy_seconds:,} seconds.")