
list_of_weapons = ["Heat Gun", "Laser", "Ice Ray"] 
import random

class Weapon():
    def __init__(self):
        self.name = ""
        self.attack_power = 17
        self.active_weapon = random.choice(list_of_weapons)
    
    
