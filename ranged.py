from weapon import Weapon

class Ranged(Weapon):
    def __init__(self, name: str, manufacturer: str, year: int, damage: int, ammo_count: int, ammo_type: str, auto: bool):
        super().__init__(name, manufacturer, year, damage)
        self.ammo_count = abs(ammo_count)
        self.ammo_type = ammo_type
        self.auto = auto
        self.magazine = abs(ammo_count)
    
    def fire(self):
        if self.ammo_count <= 0:
            print("Out of ammo! Reload!")
            return
        if self.auto:
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            super().attack()
            self.ammo_count -= 10
            return
        super().attack()
        self.ammo_count -= 1
    
    def reload(self):
        self.ammo_count = self.magazine