# ************************
# Monster class
# ************************
class Monster:

    # Constructor
    def __init__(self, monster):
        self.name = monster.get("name")
        self.description = monster.get("description")
        self.hp = monster.get("monsterHP")
        self.attack = monster.get("attack")
        self.attackDamage = monster.get("attackDamage")

    # Describe Monster
    def describe_monster(self):
        print("Name :", self.name)
        print("Description :", self.description)
        print()
