def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    
    return total

# *args = 'collect all the positional arguments into a tuple,
# and have a required named 'operator' argument:
def apply(*args, operator):
    if operator == "*":
        # REMEMBER to use *args below, because you want to multiply values of a tuple, 
        # NOT multiply one entire tuple.
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operatotor provided to apply()."
    
print(apply(1, 3, 6, 7, operator="*"))

