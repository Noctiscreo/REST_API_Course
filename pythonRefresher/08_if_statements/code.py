day_of_week = input("What day of the week is it today? ").lower()

# Checks first. If True, IGNORES the rest:
if day_of_week == "monday":
    print("Have a great start to your week!")
# If above is NOT True, checks next:
elif day_of_week == "tuesday":
    print("It's Tuesday.")
# If NEITHER the above is True, next:
else:
    print("Full speed ahead!")

print("This always runs.")

