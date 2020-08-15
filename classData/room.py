# ************************
# Room class
# ************************
class Room:

    # Constructor
    def __init__(self, room):
        # print(room)
        self.roomNumber = room.get("id")
        self.description = room.get("description")
        self.movesDict = room.get("moves")
        self.itemsDict = room.get("items")

    # Describe room
    def describe_room(self):
        print("Description :", self.description)
        print()
        if len(self.itemsDict)>0:
            print("You see the following items :")
            for key, value in self.itemsDict.items():
                print(value, key)


    # If the item matches what the player asked for
    # return that, and pop it from the itemsDict
    # so the room won't have it anymore
    def get_item(self, itemName):

        item = {}

        if itemName in self.itemsDict:
            item[itemName] = self.itemsDict[itemName]
            print("I found ", itemName)
            self.itemsDict.pop(itemName)

        return item

    # Given a move choice, return the next room number
    # TODO refactor this - we don't need to check for valid moves again
    def get_next_room(self, moveChoice):
        return self.movesDict[moveChoice]


    # Print a message if the player can't move that way
    def badMoveMessage(self):
        print("You can't go that way.... Sorry!")
        print()