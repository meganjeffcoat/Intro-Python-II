# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):

        return f"{self.name}, {self.current_room}"

    def travel(self, direction):
        nextRoom = self.current_room.roomInDirection(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(self.current_room)

        else:
            print("That direction is not allowed here")
