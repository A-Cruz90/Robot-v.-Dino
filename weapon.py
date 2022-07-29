
 
import random

class Weapon():
    def __init__(self):
        self.list_of_weapons = ["Heat Gun", "Laser", "Ice Ray"]
        self.name = ""
        self.attack_power = 17
        self.name_weapon()
    
    def name_weapon(self):
        self.name = random.choice(self.list_of_weapons)
