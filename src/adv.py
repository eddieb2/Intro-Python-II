from room import Room
from player import Player
import textwrap
import function

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
    # Prints the current room name
    # player_location = player.location
    # print(player_location.s_to)

    # Textwrap
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
    # print(type(current_move))

    if current_move[0] == 'q':
        break
    elif current_move[0] == 'n':
        # Need player location
        # check if room to the north exists
            # True: move player to north room
            # False: invalid move
            # player_location = player_location.n_to
        try:
            player.location = player.location.n_to
        except:
            print('-----------------------------------')
            print('Invalid move! No room to the North!')
            print('-----------------------------------')
    elif current_move[0] == 's':
        try:
            player.location = player.location.s_to
        except:
            print('-----------------------------------')
            print('Invalid move! No room to the South!')
            print('-----------------------------------')
    elif current_move[0] == 'e':
        try:
            player.location = player.location.e_to
        except:
            print('-----------------------------------')
            print('Invalid move! No room to the East!')
            print('-----------------------------------')
    elif current_move[0] == 'w':
        try:
            player.location = player.location.w_to
        except:
            print('-----------------------------------')
            print('Invalid move! No room to the West!')
            print('-----------------------------------')
    elif current_move[0] == 'h':
        # Encapsulate this into a function
        commands = {
            'n': 'North',
            's': 'South',
            'e': 'East',
            'w': 'West',
        }

        print('--------------------------------------')
        print('|Here is a list of available commands|')
        print('--------------------------------------')

        for key in commands:
            print(f'{key} = {commands[key]}')

# Print an error message if the movement isn't allowed.
