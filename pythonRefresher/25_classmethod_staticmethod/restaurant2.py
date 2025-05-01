class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}\nCuisine Type: {self.cuisine_type }")
    
    def open_restaurant(self):
        print("The restaurant is open!")
    
    def print_number_served(self):
        print(f"The number served is: {self.number_served}")

    def set_number_served(self, served):
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't set # served lower than current # served!")
    
    def increment_number_served(self, served):
        self.number_served += served



restaurant = Restaurant("John's Place", "Burgers")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.print_number_served()

restaurant.number_served = 100

restaurant.print_number_served()

restaurant.set_number_served(50)

restaurant.print_number_served()

restaurant.increment_number_served(20)

restaurant.print_number_served()