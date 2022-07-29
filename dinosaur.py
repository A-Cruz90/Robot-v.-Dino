list_of_dinousaurs = ["T-rex", "Stego", " Ankylosaurus"]
import random
from robot import Robot


class Dinosaur():
    def __init__(self):
        self.name = ""
        self.health = 100 
        self.attack_power = 13
        self.type_of_dino = random.choice(list_of_dinousaurs)

    def set_attack(self):
        self.attack_power = "Bite"

    def set_type(self):
        self.type_of_dino = random.choice(list_of_dinousaurs)

    def attack(self, robot):
        self.attack_power = ((robot.health) - (Dinosaur.attack_power))

    def set_name(self, name):
        self.name = name