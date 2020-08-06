'''
Day 1 MVP
Create the input command parser in adv.py which allows the program to receive player input
and commands to move to rooms in the four cardinal directions.
'''


# Add a REPL parser to adv.py that accepts directional commands to move the player
    # After each move, the REPL should print the name and description of the player's current room
    # Valid commands are n, s, e and w which move the player North, South, East or West
    # The parser should print an error if the player tries to move where there is no room.

# from room import Room

def repl_parser():
    # Player's move
    def player_move():
        current_move = input('What is your move? ')
        return current_move

    # Message displayed upon quitting
    def exit_message():
        print('--------------------')
        print('Thanks for playing!')
        print('--------------------')

    # Message displaying game instructions
    def game_instructions():
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

    # Loop continuously prompts for input unless the user exit's game
    while True:
        player_move()


repl_parser()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
