class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type }")
    
    def open_restaurant(self):
        print("The restaurant is open!")


restaurant = Restaurant("John's Place", "Burgers")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("Bob's Place", "Fish")
restaurant3 = Restaurant("Jan's Place", "Pizza")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()




