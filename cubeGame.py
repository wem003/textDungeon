import json

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




# ************************
# Player class
# ************************
class Player:

    # Constructor
    def __init__(self):
        self.inventory = []
        self.hp = 100

    # Add an item to the players inventory
    def add_item(self, item):
        self.inventory.append(item)

    # Remove an item from the players inventory
    def drop_item(self, item):
        self.inventory.remove(item)

    # Print players inventory
    def print_inventory(self):
        if len(self.inventory)>0:
            print("Your inventory is filled with :")

            # self.inventory is a list of dictionaries
            for itemDict in self.inventory:
                for key, value in itemDict.items():
                    print(value, key)
        else:
            print("You aren't carrying anything.")
        print()

    # Display current status - pretty style!
    def print_status(self):
        print()
        print("Player has", self.hp, "hit points...")
        print()


# ************************
# Monster class
# ************************
class Monster:

    # Constructor
    def __init__(self, monster):
        self.name = monster.get("name")
        self.description = monster.get("description")
        self.startRoom = monster.get("startRoom")
        self.monsterHP = monster.get("monsterHP")
        self.attack = monster.get("attack")
        self.attackDamage = monster.get("attackDamage")

    # Describe Monster
    def describe_monster(self):
        print("Name :", self.name)
        print("Description :", self.description)
        print()




# Print a kick butt intro, lol
def printIntro():
    print("Welcome to the mini dungeon, type exit to quit...")


# Print command options
def printHelp():
    print()
    print("You can enter a direction to move, like : n, ne, e, se, s, sw, w, nw")
    print("-- or --")
    print("You can enter a command such as 'get sword' or 'i' for inventory or even 'status'...")
    print()


# Print exit game message
def exitGameMessage():
    print("Ok, bye - have a nice day..")
    print()
    print("Hope you had fun you filthy animal!")


# Main function
def main():

    # define some game variables
    roomsList = []
    monstersList =[]
    player = Player()
    currentRoom = "1"
    currentRoomIndex = int(currentRoom)-1
    continueGame = ""
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

    # Open our game json
    with open('cube2.json') as data_file:
        game_data = json.load(data_file)

    # Lets build a room object for each room in the json file
    # and add it to our rooms list.  This will make it easier later.
    #
    # For each roomDetails in the list of rooms
    for roomDetails in game_data["rooms"]:
        currentRoom = Room(roomDetails)
        roomsList.append(currentRoom)

    # Lets build a monster object for each monster in the json file
    # and add it to our monsters list.
    #
    # For each roomDetails in the list of rooms
    for monsterDetails in game_data["monsters"]:
        currentMonster = Monster(monsterDetails)
        monstersList.append(currentMonster)

    # Game loop
    while continueGame != "exit":

        room = roomsList[currentRoomIndex]
        print("********************")
        print()
        room.describe_room()
        for monster in monstersList:
            if monster.startRoom == room.roomNumber:
                print("Eeek!!! A monster!")
                print()
                monster.describe_monster()
                print()
        print()
        print("********************")
        print()

        commandChoice = input("Enter a command (h for help) --> ").lower()
        commandList = commandChoice.split()

        if commandChoice in validMoves:
            # we are moving
            nextRoomNumber = room.get_next_room(commandChoice)
            if nextRoomNumber != "0":
                currentRoomIndex = int(nextRoomNumber) - 1
                print()
            else:
                room.badMoveMessage()

        elif len(commandList)>1:
            # we are doing
            commandVerb = commandList[0]
            commandNoun = commandList[1]

            if commandVerb == "get":
                newItem = room.get_item(commandNoun)
                if len(newItem)>0:
                    player.add_item(newItem)
                    player.print_inventory()
                else:
                    print(commandNoun, " isn't in this room.")
        elif commandChoice.lower() == "h":
            printHelp()
        elif commandChoice.lower() == "i":
            player.print_inventory()
        elif commandChoice.lower() == "status":
            player.print_status()
        elif commandChoice.lower() == "exit":
            # we are quitting
            break
        else:
            print("Sorry, I don't understand --> ", commandChoice)

    exitGameMessage()


if __name__ == "__main__":
    main()