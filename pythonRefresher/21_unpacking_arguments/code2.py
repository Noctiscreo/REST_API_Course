# You can destructure arguments passed into a function call.
# e.g. add(*nums)
# Note that *nums must still have an equal number 
# of parameters to arguments for the function call.

# Write a function as normal.
def add(x, y):
    return x + y

nums = [3, 5]

# *nums takes both numbers from the nums list, 
# which matches the required number of arguments.
print(*nums)
print(add(*nums))

