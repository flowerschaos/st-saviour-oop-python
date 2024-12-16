from weapon import Weapon
from ranged import Ranged
from melee import Melee

if __name__ == '__main__':
    # defines "revolver"
    revolver = Ranged(
        name = 'Phantom',
        manufacturer = 'Reverb Workshop',
        year = 2142,
        damage = 5,
        ammo_count = 6,
        ammo_type = '.44 Magnum',
        auto = False
    )
    # defines "sledgehammer"
    sledgehammer = Melee(
        name = 'Home Improvement',
        manufacturer = 'Reverb Workshop',
        year = 2143,
        damage = 8,
        length = 2
    )
    # defines "glockinator"
    glockinator = Ranged(
        name = 'The Glockinator',
        manufacturer = 'Beast Mechanisms',
        year = 2150,
        damage = 10,
        ammo_count = 20,
        ammo_type = '9mm',
        auto = True
    )
    # defines "brella"
    brella = Melee(
        name = 'Tactical Umbrella',
        manufacturer = 'Beast Mechanisms',
        year = 2150,
        damage = 7,
        length = 3
    )
    # attacks
    revolver.attack()
    sledgehammer.attack()
    glockinator.attack()
    brella.attack()