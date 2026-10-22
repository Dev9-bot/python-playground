class Character:
    _character_count = 0

    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        Character._character_count += 1

    def show(self):
        print(f"I am {self.name}, I am level {self.level} and my health is {self.health}.")

    @classmethod
    def class_counter(cls):
        return Character._character_count

class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength

    def show(self):
        print(f"I am {self.name}, I am level {self.level}, my health is {self.health} and my strength is {self.strength}.")

class Mage(Character):
    def __init__(self, name, level, health, mana):
        super().__init__(name, level, health)
        self.mana = mana

    def show(self):
        print(f"I am {self.name}, I am level {self.level}, my health is {self.health} and my mana is {self.mana}.")

class Party:
    def __init__(self, name, level, health, members):
        self.name = name
        self.level = level
        self.health = health
        self.members = members

    def add_member(self, member):
        self.members.append(member)
    @classmethod
    def show_party(cls, party):
        print(f"Party Name: {party.name}, Level: {party.level}, Health: {party.health}")
        print("Members:")
        for member in party.members:
            member.show()        

    @staticmethod
    def calculate_damage(attack_power, defense):
        return max(0, attack_power - defense)

W = Warrior("Ares", 5, 100, 20)
M = Mage("Merlin", 5, 80, 100)
P = Party("The Heroes", 5, 280, [W, M])
Party.show_party(P)
print(f"Damage dealt: {Party.calculate_damage(50, 30)}")
print(f"Total characters created: {Character.class_counter()}")