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
        self.itemsList = []
        self.monster = None
        self.event = room.get("event")
        self.eventDescription = room.get("eventDescription")

    # Describe room
    def describe_room(self):
        print("Description :", self.description)
        print()
        if len(self.itemsList) > 0:
            print("You see the following items :")
            for item in self.itemsList:
                print(item.name)

    def printDebug(self):
        print("***********************")
        print("Room Number:", self.roomNumber)
        print("Description:", self.description)
        print("Moves Dictionary:", self.movesDict)
        if len(self.itemsList) > 0:
            print("Items List:")
            for item in self.itemsList:
                print("\t-->", item.name)
        else:
            print("Items: No items present")
        if self.monster is not None:
            print("Monster:", self.monster.name)
            print("\t-->", self.monster.description)
        else:
            print("Monster: No monster present")
        print("Event:", self.event)
        print("Event Description:", self.eventDescription)
        print()



    # Place an item in the room
    def place_item(self, item):
        self.itemsList.append(item)

    # If the item matches what the player asked for
    # return that, and pop it from the itemsDict
    # so the room won't have it anymore
    def get_item(self, itemName):

        returnItem = None

        for item in self.itemsList:
            roomItem = item.name
            if roomItem.lower() == itemName:
                print("I found ", itemName)
                returnItem = item
                self.itemsList.remove(item)

        return returnItem

    # Place a monster in the room
    def place_monster(self, monster):
        self.monster = monster

    # Given a move choice, return the next room number
    # TODO refactor this - we don't need to check for valid moves again
    def get_next_room(self, moveChoice):
        return self.movesDict[moveChoice]

    # Print a message if the player can't move that way
    def badMoveMessage(self):
        print("You can't go that way.... Sorry!")
        print()
