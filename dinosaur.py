import random
from robot import Robot


class Dinosaur():
    def __init__(self):
        self.list_of_dinousaurs = ["T-rex", "Stego", " Ankylosaurus"]
        self.name = ""
        self.health = 100 
        self.attack_power = 13
        self.set_type()

    def set_attack(self):
        self.attack_power = "Bite"

    def set_type(self):
        self.name = random.choice(self.list_of_dinousaurs)

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacked {robot.name} for {self.attack_power} leaving {robot.name} with {robot.health} health remaining ')

   