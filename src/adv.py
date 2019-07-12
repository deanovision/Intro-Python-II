from room import Room
from player import Player
from item import Item
from os import system, name

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     Item("sword", "legendary sword of king arthur")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("knife", "famous knife of crocodile dundee. thats not a knife, this is a knife!")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("elixir", "the bottled tears of your enemies")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("spellbook", "legendary book of magic")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("key", "mysterious looking key")),
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
player = Player("Rodean", room["outside"])


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

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while True:
    current_room = player.current_room
    print(current_room)
    current_room.print_items()

    valid_directions = ["n", "s", "e", "w"]
    valid_actions = ["get", "drop"]
    cmd = input("Type n,s,e,w to move or q to quit:").split(" ")
    current_action = cmd[0]
    if len(cmd) > 1:
        item_of_interest = cmd[1]
    if current_action in valid_directions:
        clear()
        player.move_player(current_action)
    elif current_action == "q":
        clear()
        print("Goodbye")
        break
    elif current_action == "i":
        clear()
        player.list_inventory()

    elif current_action in valid_actions:
        clear()
        # remove item from room list and add to player inventory
        if current_action == "get":
            located_item = current_room.locate_item(item_of_interest)
            if located_item:
                player.add_to_inventory(located_item)
                current_room.remove_item(located_item)
            else:
                print("Item not found")
        elif current_action == "drop":
            dropped_item = player.remove_from_inventory(item_of_interest)
            current_room.add_item(dropped_item)

    else:
        clear()
        print("command not recognized", "\n")
