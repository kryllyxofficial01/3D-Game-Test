import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import Voxel

# Setup code
game = ursina.Ursina()
player = FirstPersonController()
info = ursina.Text(
    text = "Press ESC to exit the game...",
    origin = (2.17,-19)
)

# Simple configurations
ursina.mouse.locked = True
ursina.window.fullscreen = True
ursina.window.title = "3D Game"
platform_size = 20

# Generate a basic platform
for x in range(platform_size):
    for z in range(platform_size):
        voxel = Voxel(
            position = (x,0,z)
        )

# Runs every tick
def update():
    if ursina.held_keys["escape"]:
        game.userExit()

# Start the engine
game.run()