friends = ["Rolf", "Bob"]

def add_friend():
    friend_name  = input("Enter your friend name: ")
    friends.append(friend_name)

add_friend()

print(friends)