class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        # !r calls the repr method of self.name
        # so that is shows with quotes. 
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


# Create a new class called 'printer' 
# that inherits properties and methods of 'Device'.
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # Inherit 'Device's __init__:
        super().__init__(name, connected_by)
        # We still need 'capacity':
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        # Return the super class's __str__ method
        # "return f"Device {self.name!r} ({self.connected_by})"
        # and also 'remaining_pages':
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            # use 'return' to exit the function.
            return
        
        print(f"Printing {pages} pages...")
        # -= removes a # of pages from the printer:
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

# When looking for the 'disconnect' method:
# first the Printer class will be checked,
# then the Device class will be checked,
# then the python object will be checked.
printer.disconnect()

# Can't print after printer is disconnected:
printer.print(30)