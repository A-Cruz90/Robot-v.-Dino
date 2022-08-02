
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon


class Battlefield():
    def __init__(self, name):
        self.name = name
        self.robot = Robot()
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
        while True:
            if self.robot.health <= 0:
                loser = self.robot.name
                champion = self.dino.name
                print(f'Game Over... Loser: {self.robot.name} therefore your Champion: {self.dino.name}')
            elif self.dino.health <= 0:
                loser = self.dino.name
                champion = self.robot.name
                print(f'Game Over Loser: {self.dino.name} therefore your Champion:{self.robot.name}')
            elif self.robot.health >= 0 or self.dino.health >= 0:
                self.dino.attack(self.robot)
                self.robot.attack(self.dino)
    
