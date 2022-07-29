from weapon import Weapon



class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} for {self.active_weapon.attack_power} leaving {dinosaur.name} with {dinosaur.health} health remaining ')

    def set_name(self, name):
        self.name = name
