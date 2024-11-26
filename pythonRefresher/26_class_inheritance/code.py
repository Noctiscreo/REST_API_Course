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
    

printer = Device("Printer", "USB")

print(printer)
printer.disconnect()