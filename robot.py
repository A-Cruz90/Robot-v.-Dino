from weapon import Weapon


class Robot():
    def __init__(self, name):
        self.name = ""
        self.health = 100
        self.active_weapon = Weapon("laser", "")

    def attack(self, dinosaur):
        self.attack = ((dinosaur.health) - (robot.active_weapon))

    def set_name(self, name):
        self.name = name

    def hold_weapon(self):
        self.active_weapon 