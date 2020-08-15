# ************************
# Item class
# ************************
class Item:

    # Constructor
    def __init__(self, item):

        self.name = item.get("name")
        self.description = item.get("description")
        self.attackDamage = item.get("attackDamage")
        self.qty = item.get("qty")


    # Describe item
    def describe_item(self):
        print("", self.name, ":", self.qty, "of", self.description)
        print()