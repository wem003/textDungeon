import json
from classData.room import Room
from classData.player import Player
from classData.monster import Monster


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
    with open('./gameData/cube2.json') as data_file:
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