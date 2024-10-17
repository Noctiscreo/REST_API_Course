# Conceptually, 'defining' the code:
def user_age_in_seconds():
    user_age = int(input("Input your age: "))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds: {age_in_seconds:,}")

# Conceptually, 'running' the code:
user_age_in_seconds()

