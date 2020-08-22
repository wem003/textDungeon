# ************************
# Player class
# ************************
class Player:

    # Constructor
    def __init__(self):
        self.inventory = []
        self.hp = 100
        self.weapon = None

    # Add an item to the players inventory
    def add_item(self, item):
        self.inventory.append(item)

    # Remove an item from the players inventory
    def drop_item(self, item):
        self.inventory.remove(item)

    # Equip a weapon from Player Inventory
    def equip_weapon(self, item):
        for playerItem in self.inventory:
            if playerItem.name.lower() == item:
                self.weapon = item
                print("Player has equipped ", self.weapon)

    # Print players inventory
    def print_inventory(self):
        if len(self.inventory) > 0:
            print("Your inventory is filled with :")
            for item in self.inventory:
                item.describe_item()
        else:
            print("You aren't carrying anything.")
        print()

    def describe_weapon(self):
        if self.weapon is not None:
            print("Player is currently using ", self.weapon)

    # Display current status - pretty style!
    def print_status(self):
        print()
        print("Player has", self.hp, "hit points...")
        print()
        self.print_inventory()
        print()
        self.describe_weapon()
        print()