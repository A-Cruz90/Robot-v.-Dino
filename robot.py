from weapon import Weapon
from weapon import list_of_weapons
import random


class Robot():
    def __init__(self):
        self.name = ""
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        self.attack = ((dinosaur.health) - (Robot.active_weapon))

    def set_name(self, name):
        self.name = name

    def hold_weapon(self):
        self.active_weapon = random.choice(list_of_weapons)