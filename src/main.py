import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import Voxel

game = ursina.Ursina()
player = FirstPersonController()

for z in range(20):
    for x in range(20):
        voxel = Voxel(
            position = (x,0,z)
        )

game.run()