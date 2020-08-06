# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.hidden_items = {
            0: 'bag of gold',
            1: 'sword',
            2: 'diamond ring',
            3: 'golf watch',
            4: 'ink quill',
            5: 'paper',
            6: 'recurve bow',
            7: 'quiver',
        }

    def remove_hidden_item(self, item_key):
        self.hidden_items.pop(item_key)

    def add_hidden_item(self, dropped_item):
        new_key = None

        # fail safe: protects against the case that all rng == key throughout the dict loop
        while new_key is None:
        # if random_num != any key in dict, use rng for dropped item key
            for key in self.hidden_items:
                # rgn
                random_num = random.randint(0, 15)

                if key != random_num:
                    new_key = random_num

        self.hidden_items[new_key] = dropped_item

    def __str__(self):
        return f'Room: {self.name}, Description: {self.description}'
