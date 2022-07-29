
from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

weapon_one = Weapon()
weapon_two = Weapon()
weapon_three = Weapon()

print(weapon_one.active_weapon)

battlefield_one = Battlefield()
battlefield_two = Battlefield()
battlefield_three = Battlefield()

battlefield_one.set_name("Plain Fields")
battlefield_two.set_name("Mountains")
battlefield_three.set_name("Lava Plains")

robot_one = Robot()
robot_two = Robot()
robot_three = Robot()

robot_one.set_name("Bender")
robot_two.set_name("Roger")
robot_three.set_name("Odin")

dino_one = Dinosaur()
dino_two = Dinosaur()
dino_three = Dinosaur()

dino_one.set_name("Chompy")
dino_two.set_name("Bob")
dino_three.set_name("Finn")

robot_one.hold_weapon()
robot_two.hold_weapon()
robot_three.hold_weapon()

print(robot_one.active_weapon)
print(robot_three.active_weapon)
print(robot_two.active_weapon)

print(robot_one.health)
print(robot_two.health)
print(robot_three.health)

print(robot_one.active_weapon.attack_power)

