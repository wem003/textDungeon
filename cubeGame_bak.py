import json

# global variables
itemCatalog = ["coins", "sword", "wand"]
playerInventory = {}

# Function to validate move choices
# Returns True if a valid move choice
def validMove(moveChoice):
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

    if moveChoice in validMoves:
        print()
        return True
    elif moveChoice =="exit":
        exitGameMessage()
    else:
        print("Sorry, that wasn't a valid move choice...  Try again..")
        print()

    return False


# Given a move choice, return the next room to move to
def getNextRoom(moveList, moveChoice):
    for moveDict in moveList:
        return moveDict[moveChoice]


# Describe the room and any contents
def describeRoom(room_data, currentRoomIndex):
    print("You are in here :", room_data["rooms"][currentRoomIndex]["description"])
    roomItemList = room_data["rooms"][currentRoomIndex]["items"]

    if len(roomItemList) > 0:
        for itemDict in roomItemList:
            for itemCatalogOption in itemCatalog:
                if itemCatalogOption in itemDict:
                    print("This room has the following: ", itemCatalogOption, " with this value: ", itemDict[itemCatalogOption])
                    playerInventory[itemCatalogOption] = itemDict[itemCatalogOption]

    else:
        print("This room looks pretty empty...")


# Print player inventory
def printInventory():
    if len(playerInventory) > 0 :
        for item in playerInventory:
            print("Player has an item! ", item, " with this attribute :", playerInventory[item])
    else:
        print("Poor player, you have no inventory...")



# Print a kick butt intro, lol
def printIntro():
    print("Welcome to the mini dungeon, type exit to quit...")


def badMoveMessage():
    print("You can't go that way.... Sorry!")
    print()


# Print exit game message
def exitGameMessage():
    print("Ok, bye - have a nice day..")
    print()
    print("Hope you had fun you filthy animal!")


# Main function
def main():

    #define some game variables
    currentRoom = "1"
    currentRoomIndex = int(currentRoom)-1
    continueGame = ""

    # Open our game json
    with open('cube.json') as data_file:
        room_data = json.load(data_file)

    # Game loop
    while continueGame != "exit":
        describeRoom(room_data, currentRoomIndex)
        printInventory()
        print()


        moveChoice = input("Enter a direction to move (n,ne,e,se,s,sw,w,nw) --> ").lower()

        if validMove(moveChoice):
            moveList = room_data['rooms'][currentRoomIndex]['moves']
            nextRoom = getNextRoom(moveList, moveChoice)

            if nextRoom!="0":
                currentRoomIndex = int(nextRoom)-1
            else:
                badMoveMessage()

        elif moveChoice.lower() == "exit":
            break


if __name__ == "__main__":
    main()