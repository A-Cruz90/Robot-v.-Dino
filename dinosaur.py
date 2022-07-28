list_of_dinousaurs = ["T-rex", "Stego", " Ankylosaurus"]
import random

from robot import Robot

class Dinosaur():
    def __init__(self, name, attack_power):
        self.name = ""
        self.health = 100 
        self.attack_power = 13

    def set_attack(self):
        self.attack_power = "Bite"

    def set_type(self):
        self.type = random.choice(list_of_dinousaurs(range(0,2)))

    def attack(self, robot):
        self.attack_power = ((robot.health) - (dinosaur.attack_power))

    