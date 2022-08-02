from weapon import Weapon
import random


class Robot():
    def __init__(self):
        self.list_of_robots = ["Bender ", "Joey "]
        self.name = ""
        self.health = 100
        self.active_weapon = Weapon()
        self.set_type()

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} for {self.active_weapon.attack_power} leaving {dinosaur.name} with {dinosaur.health} health remaining ')

    def set_type(self):
        self.name = random.choice(self.list_of_robots)
