# 'is' is not the same as ==. 'is' checks if two things are the same object.
# 'is' is rarely used.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

# True
print(friends == abroad)

# False
print(friends is abroad)

# True
print(friends is friends)