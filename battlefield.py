from dinosaur import Dinosaur
from robot import Robot


class Battlefield():
    def __init__(self):
        self.name = ""
        self.opponent_one = Robot("")
        self.opponent_two = Dinosaur("", "")

    def set_name(self,name):
        self.name = name

    def run_game(self):
        pass

    def display_welcome(self):
        print(f'Welcome to SlugFest. May the strongest survive! ')

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
    