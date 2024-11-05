# Username mapping to perform a login.

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

# Create a new dictionary.
# For each user in users, take the name from user[1]
# and assign the entire user tuple as the value.
# user[1] (the user's name) = Key
# user info = Value
# for user in users = for loop
username_mapping = {user[1]: user for user in users}

print(username_mapping)
# Can get all the information of "Bob" at once:
#print(username_mapping["Bob"])

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]
print(_, username, password)

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")