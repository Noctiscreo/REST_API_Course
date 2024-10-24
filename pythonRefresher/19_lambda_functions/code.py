sequence = [1, 3, 5, 9]

# Below is less readable:
doubled1 = [(lambda x: x * 2)(x) for x in sequence]
# More readable:
doubled2 = list(map(lambda x: x *2, sequence))

print(doubled1)
print(doubled2)