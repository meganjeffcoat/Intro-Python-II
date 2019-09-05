# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):

        return f"Name: {self.name}, Room:{self.current_room}, Inventory: {self.inventory}"

    def travel(self, direction):
        nextRoom = self.current_room.roomInDirection(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(self.current_room, self.current_room.items)

        else:
            print("That direction is not allowed here")

    def get_item(self, item_name):
        if item in self.inventory:
            if item.name == item_name:
                return item_name
        return None
