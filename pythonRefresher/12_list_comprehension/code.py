# List Comprehension method:
friends = ["Rolf", "Same", "Samantha", "Saurabh", "Jen"]
# First 'name' is what you want to add to the new created list.
starts_with_s = [name for name in friends if name.startswith("S")]

print(starts_with_s)
