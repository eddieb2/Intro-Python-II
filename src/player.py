# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def __str__(self):
        return f'Location: "{self.location}"'

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, item):
        return self.inventory.append(item)

    def remove_inventory_item(self, item):
        return self.inventory.remove(item)
    # When I call this instance method, it references the instance method in
    # the class Room called def __str__
    def get_location(self):
        return self.location
