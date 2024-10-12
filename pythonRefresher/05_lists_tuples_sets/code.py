# List - Can be modified. 
# Order is always the same.
l = ["Bob", "Rolf", "Anne"]

# Tuple - Can't be modified.
t = ("Bob", "Rolf", "Anne")

# Set, aka Dictionary.
# You can add to a dictionary, 
# but you can't have duplicates, e.g. "Bob" and "Bob".
# The order of elements might change, e.g. when printed out.
s = {"Bob", "Rolf", "Anne"}

# the [0] is called 'subscript notation'
print(l[0])

# Add to a list:
l[0] = "Saunders"
print(l)

# Append to the end of a list:
l.append("Hasznosi")
print(l)

# You can't append to tuples or sets/dictionaries!

# Add to a set/dictionary:
s.add("Jackson")
# The second add is ignored, because you can't have duplicates:
s.add("Jackson")
print(s)

# To remove from a list:
l.remove("Saunders")
print(l)

