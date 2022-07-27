list_of_weapons = ["Heat Gun", "Laser", "Ice Ray"] 
import random


class Weapon():
    def __init__(self):
        self.name = ""
        self.attack_power = ""
        self.active_weapon = []
        
    def set_weapon(self):
        self.active_weapon = random.choice(list_of_weapons(range(0,2)))

        