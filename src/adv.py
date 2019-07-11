from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [{"name": "sword", "description": "legendary sword of king arthur"}]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [{"name": "knife", "description": "famous knife of crocodile dundee. thats not a knife, this is a knife!"}]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [{"name": "elixir", "description": "the bottled tears of your enemies"}]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [{"name": "spellbook", "description": "legendary book of magic used by Merlin"}]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [{"name": "key", "description": "mysterious looking key"}]),
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


# def next_room(current_room, direction):
#     rooms = {
#         "outside": {
#             "n": "foyer"
#         },
#         "foyer": {
#             "n": "overlook",
#             "s": "outside",
#             "e": "narrow"
#         },
#         "overlook": {
#             "s": "foyer"
#         },
#         "narrow": {
#             "w": "foyer",
#             "n": "treasure"
#         },
#         "treasure": {
#             "s": "narrow"
#         }
#     }
#     return rooms[current_room][direction]


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

# def moves(cmd):


player_1 = Player("Rodean", room["outside"])

while True:
    print("current location:", player_1.current_room.name)
    print(player_1.current_room.description)
    player_cmd = input("Type n,s,e,w to move or q to quit:")
    if player_cmd == "n":
        if player_1.current_room.n_to:
            print("you moved to the north")
            player_1.current_room = player_1.current_room.n_to
        else:
            print("you can't move there")
    elif player_cmd == "s":
        if player_1.current_room.s_to:
            print("you moved to the south")
            player_1.current_room = player_1.current_room.s_to
        else:
            print("you can't move there")
    elif player_cmd == "e":
        if player_1.current_room.e_to:
            print("you moved to the east")
            player_1.current_room = player_1.current_room.e_to
        else:
            print("you can't move there")
    elif player_cmd == "w":
        if player_1.current_room.w_to:
            print("you moved to the east")
            player_1.current_room = player_1.current_room.w_to
        else:
            print("you can't move there")
    elif player_cmd == "q":
        break
    else:
        print("command not recognized")
