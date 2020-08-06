from room import Room
from player import Player
import textwrap
import random

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
while True:
    # TEST SHOWING THAT ADD HIDDEN ITEMS WORKS FINE
    # player.location.add_hidden_item('hi')
    # player.location.add_hidden_item('hi')
    # player.location.add_hidden_item('hi')
    print(player.location.hidden_items)
    # FOR TESTING - SHOWS ALL ROOMS & THEIR ITEMS
    print('Outside: ', end='')
    print(room['outside'].hidden_items.keys())
    print('Foyer: ', end='')
    print(room['foyer'].hidden_items.keys())
    print('Overlook: ', end='')
    print(room['overlook'].hidden_items.keys())
    print('Narrow: ', end='')
    print(room['narrow'].hidden_items.keys())
    print('Treasure: ', end='')
    print(room['treasure'].hidden_items.keys())

    # Textwrap
    # Prints the current room name
    # Prints the current description (the textwrap module might be useful here).
    wrapper = textwrap.TextWrapper(width=40)
    word_list = wrapper.wrap(text=str(player.location))
    print('')

    for item in word_list:
        print(item)

    print('')

    # Waits for user input and decides what to do.
    current_move = input('Enter Move: ').split(',')
    print('')

    if current_move[0] == 'q':
        break
    elif current_move[0] == 'n':
        try:
            player.location = player.location.n_to
        except AttributeError:
            print('-----------------------------------')
            print('Invalid move! No room to the North!')
            print('-----------------------------------')
    elif current_move[0] == 's':
        try:
            player.location = player.location.s_to
        except AttributeError:
            print('-----------------------------------')
            print('Invalid move! No room to the South!')
            print('-----------------------------------')
    elif current_move[0] == 'e':
        try:
            player.location = player.location.e_to
        except AttributeError:
            print('-----------------------------------')
            print('Invalid move! No room to the East!')
            print('-----------------------------------')
    elif current_move[0] == 'w':
        try:
            player.location = player.location.w_to
        except AttributeError:
            print('-----------------------------------')
            print('Invalid move! No room to the West!')
            print('-----------------------------------')
    elif current_move[0] == 'x':
        # generate a rand num
        rand_num = random.randint(0, 15)
        # have to remove the items after the for loop completes,
        # otherwise an error is thrown due to the dict length changing
        remove_room_item = None

        for key, value in room['outside'].hidden_items.items():
            # if rand num == key of the hidden item, add item (value) to player's inventory
            if rand_num == key:
                # prompt to pick up or drop the item
                item_action = input(f'You found a {value}! \n Pick up = [p] | Drop = [d]: ')
                # need confirmation screen (optional)
                if item_action == 'p':
                    player.set_inventory(value)
                    # add item to a list of items to remove from room's inv
                    remove_room_item = key
                    print('Item is now in your inventory!', end='\n\n')
                elif item_action == 'd':
                    print('Item dropped')
                    break

        # remove the item that was picked up from the room's inv
        if remove_room_item != None:
            player.location.remove_hidden_item(remove_room_item)

    elif current_move[0] == 'inv':
        # Grabs player's current inventory
        current_inventory = player.get_inventory()

        # Loop and display inventory
        print('>> Inventory')
        print('--------------------')

        inv_count = 0
        for item in current_inventory:
            print(f'{inv_count + 1}: {item}')

        print('--------------------')

        # Drop item ? Continue?
        drop_inventory_item = input('Would you like to remove an item from you inventory? [y] [n] >> ')
        if drop_inventory_item == 'y':
            # What item do you want to drop?
            item_to_drop = input('What item do you want to remove? [type item name] >> ')
            # Drop item from inv
            player.remove_inventory_item(item_to_drop)
            # Add item to current room
            player.location.add_hidden_item('item_to_drop')
        elif drop_inventory_item == 'n':
            continue

    # FIXME: This should probably be an else
    elif current_move[0] == 'h' or 'help':
        # Encapsulate this into a function
        commands = {
            'n': 'Move North',
            's': 'Move South',
            'e': 'Move East',
            'w': 'Move West',
            'p': 'Pick up item.',
            'd': 'Drop item.',
            'inv': 'Show inventory.',
            'h': 'Show help menu.',
            'q': 'Quit game.'
        }

        print('--------------------------------------')
        print('|Here is a list of available commands|')
        print('--------------------------------------')

        for key in commands:
            print(f'{key} = {commands[key]}')
