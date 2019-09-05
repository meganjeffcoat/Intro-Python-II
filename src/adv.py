from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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

# Items

item = {
    'map': Item("Map", "Look a map to guide you!"),
    'sword': Item("Sword", "You found the sword"),
    'wand': Item("Want", "You found a magic wand"),
    'food': Item("Food", "You found some food, go ahead and eat"),
    'cloak': Item("Cloak", "You found an invisibility cloak"),
    'candle': Item("Candle", "You found a candle"),
    'hammock': Item("Hammock", "Look a hammock, rest a spell"),
}

# Link items to rooms

room['outside'].items.append(item['map'])
room['foyer'].items.append(item['food'])
room['foyer'].items.append(item['sword'])
room['overlook'].items.append(item['hammock'])
room['narrow'].items.append(item['candle'])
room['treasure'].items.append(item['cloak'])
room['treasure'].items.append(item['wand'])

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

current_room = room['outside']
name = input("Please add character name: ")
player = Player(name, current_room)
playerRoom = Room(current_room.name, current_room.description)

while True:

    # print(f"Items in {current_room.name}: {current_room.items}")

    direction = input(
        "Please choose a direction, North(n), South(s), West(w), East(e), Quit(q): ")
    if direction in ["n", "s", "w", "e"]:
        player.travel(direction)
        continue
    elif direction == "q":
        break
    else:
        print("You cannot go that direction")

print("Thanks for playing, come play again!")
