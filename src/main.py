import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import Voxel

game = ursina.Ursina()
player = FirstPersonController()

for x in range(8):
    for z in range(8):
        voxel = Voxel(
            position = (x,0,z)
        )

def update():
    if ursina.held_keys["escape"]:
        game.userExit()

game.run()