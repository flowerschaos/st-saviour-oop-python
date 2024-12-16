from weapon import Weapon

class Melee(Weapon):
    def __init__(self, name: str, manufacturer: str, year: int, damage: int, length: int):
        super().__init__(name, manufacturer, year, damage)
        self.length = abs(length)
        self.battery = 100.0

    def charge(self):
        if self.battery <= 0:
            print("Out of charge...")
            return
        if self.battery >= 100:
            self.damage = self.damage * 2
            self.battery -= 0.5
        if self.battery <= 50:
            self.damage = self.damage * 1.5
            self.battery -= 0.5
    
    def recharge(self, duration: int):
        self.battery += duration * 0.5