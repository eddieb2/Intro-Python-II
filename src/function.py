# def repl_parser():
#     # Player's move
#     def player_move():
#         current_move = input('What is your move? ')
#         return current_move
#
#     # Message displayed upon quitting
#     def exit_message():
#         print('--------------------')
#         print('Thanks for playing!')
#         print('--------------------')
#
#     # Message displaying game instructions
#     def game_instructions():
#         commands = {
#             'n': 'North',
#             's': 'South',
#             'e': 'East',
#             'w': 'West',
#         }
#
#         print('--------------------------------------')
#         print('|Here is a list of available commands|')
#         print('--------------------------------------')
#
#         for key in commands:
#             print(f'{key} = {commands[key]}')
#
#     # Loop continuously prompts for input unless the user exit's game
#     while True:
#         player_move()
#
#
# repl_parser()

# Message displaying game instructions
# def game_instructions():
#     commands = {
#         'n': 'North',
#         's': 'South',
#         'e': 'East',
#         'w': 'West',
#     }
#
#     print('--------------------------------------')
#     print('|Here is a list of available commands|')
#     print('--------------------------------------')
#
#     for key in commands:
#         print(f'{key} = {commands[key]}')

# l1 = [1,2,3,4]
# for item in l1:
#     print(item)
#     if item == 5:
#         print('item already exists')
#     else:
#         l1.append(5)


s1 = set()
s1.add('hi')
s1.remove('hi')
print(s1)
# for item in s1:
#     print(item)