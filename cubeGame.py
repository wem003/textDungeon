import json


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
        print("You are in here :", room_data["rooms"][currentRoomIndex]["description"])
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