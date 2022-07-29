from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon


class Battlefield():
    def __init__(self, name):
        self.name = name
        self.robot = Robot("Bob")
        self.dino = Dinosaur()

    # all of our game functions get called insdie run_game
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        


    def display_welcome(self):
        print(f'Welcome to SlugFest. May the strongest survive! ')

    # while loop is great to make them fight until one of their health values drops to 0
    def battle_phase(self):
        # while loop here
        self.robot.attack(self.dino)
        self.dino.attack(self.robot)

    def display_winner(self):
        pass
    