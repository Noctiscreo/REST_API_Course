def add(x, y):
    return x + y

nums = {"x": 3, "y":5}

print(add(nums["x"], nums["y"]))
# Or instead:
print(add(**nums))

# **nums passes in each VALUE from the nums dictionary 
# as an argument to the 'add' function.

