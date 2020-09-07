import json
import random
from classData.room import Room
from classData.player import Player
from classData.monster import Monster
from classData.item import Item

# Define some global vars
roomsList = []
monstersList = []
itemList = []


# Game initialization
def game_init():
    printIntro()

    roomCount = len(roomsList)

    # First lets place items.  Items can go in any room
    for item in itemList:
        randomRoom = random.randint(0, roomCount - 1)
        currentRoom = roomsList[randomRoom]
        currentRoom.place_item(item)
        roomsList[randomRoom] = currentRoom

    # Now lets place monsters
    for monster in monstersList:
        # We don't want monsters in the start room, so start at index 1 instead of 0
        randomRoom = random.randint(1, roomCount - 1)
        currentRoom = roomsList[randomRoom]

        # In this game, only one monster per room
        if currentRoom.monster is None:
            currentRoom.place_monster(monster)
            roomsList[randomRoom] = currentRoom

# Return true if fighting
def fightCheck(player):

    fight = False
    commandChoice = input("You've encountered a monster - do you want to fight? (y or n) --> ").lower()

    while (commandChoice != 'y') or (commandChoice != 'n'):
        if commandChoice == 'y':
            fight = True
            break
        elif commandChoice == 'n':
            savingRoll = random.randint(1, 10)
            if savingRoll < 7:
                player.print_status()
                fight = True
                newPlayerHP = player.hp - (player.hp * .1)
                player.hp = int(newPlayerHP)
                print("After saving roll fail")
                player.print_status()
                break
        else:
            print("You need to enter y or n...")
            print()

    return fight


# Combat routine, return a flag indicating win or lose
def combat(player, monster):

    print("COMBAT!")
    victoryFlag = False

    # Default Attack points if no weapon equipped
    playerDefaultAttackPoints = 5

    while player.hp > 0 and monster.hp > 0:
        print()
        print("Player HP:", player.hp, " <---> Monster HP:", monster.hp)
        print()

        playerAttackChance = random.randint(1, 10)
        monsterAttackChance = random.randint(1, 10)

        # Player Attacks First
        if player.weapon is None:
            print("You're in trouble... You only have fists of pudding!")
            monster.hp = monster.hp - playerDefaultAttackPoints
        elif playerAttackChance < 7:

            playerAttackPoints = player.get_weapon_attack_hp()
            monster.hp = monster.hp - playerAttackPoints

            print("The player attacked with", player.weapon.name, "which has an attack damage of", playerAttackPoints)
        else:
            print("The players attack missed!")

        # Now its the monsters turn!
        if monster.hp > 0:
            if monsterAttackChance < 7:
                print("The monster attacked with", monster.attack, "which has an attack damage of", monster.attackDamage)
                player.hp = player.hp - monster.attackDamage
            else:
                print("The monsters attack missed!")

        input("Press <ENTER> to continue the fight!!!")

    if player.hp > 0:
        print("You have won!")
        victoryFlag = True
    elif monster.hp > 0:
        print("The monster has won!")

    return victoryFlag


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
    player = Player()
    currentRoom = "1"
    currentRoomIndex = int(currentRoom) - 1
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
    # For each monsterDetails in the list of rooms
    for monsterDetails in game_data["monsters"]:
        currentMonster = Monster(monsterDetails)
        monstersList.append(currentMonster)

    # Lets build an item object for each item in the json file
    # and add it to our item list.
    #
    # For each itemDetails in the list of rooms
    for itemDetails in game_data["items"]:
        currentItem = Item(itemDetails)
        itemList.append(currentItem)

    game_init()

    # Game loop
    while continueGame != "exit":

        room = roomsList[currentRoomIndex]
        print("********************")
        print()
        room.describe_room()
        if room.monster == None:
            print("Phew, no monsters here...")
        else:
            print("Eeek!!! A monster!")
            print()
            room.monster.describe_monster()
            print()
            if fightCheck(player):
                if combat(player, room.monster):
                    # What to do if we win
                    room.monster = None
                else:
                    # What to do if we've lost
                    break
            elif player.hp > 0:
                print()
                print("You've avoided combat for now, but have taken a hit... ")
                print("You now have", player.hp, "HP.  What do you want to do?")
                print()

        print()
        print("********************")
        print()

        #hp check - continue or dead

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

        elif len(commandList) > 1:
            # we are doing some action - not moving
            commandVerb = commandList[0]
            targetItem = ""

            # If we have two items in the command list, its a verb and noun
            if len(commandList) == 2:
                targetItem = commandList[1]

            # If we have 3 items in the command list, we'll assume verb, adjective, noun
            if len(commandList) == 3:
                targetItem = commandList[1] + ' ' + commandList[2]

            if commandVerb == "get":
                newItem = room.get_item(targetItem)
                if newItem is not None:
                    player.add_item(newItem)
                    player.print_inventory()
                else:
                    print(targetItem, " isn't in this room.")
            elif commandVerb == "equip":
                player.equip_weapon(targetItem)

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
