list_of_dinousaurs = ["T-rex", "Stego", " Ankylosaurus"]
import random

class Dinosaur():
    def __init__(self):
        self.name = ""
        self.health = 100 
        self.attack_power = 120
        self.type = []

    def set_attack(self):
        self.attack_power = "bite"

    def set_type( self ):
        self.type = random.choice(list_of_dinousaurs(range(0,2)))

    def attack( self, robot ):
        pass

    