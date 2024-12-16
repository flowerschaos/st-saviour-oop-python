class Weapon:
    def __init__(self, name: str, manufacturer: str, year: int, damage: int):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.damage = damage

    def attack(self):
        print(self.name+" does "+self.damage+" points of damage!")