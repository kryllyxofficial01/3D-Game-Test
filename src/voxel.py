import ursina
from ursina import *

class Voxel(Button):
    def __init__(self, position=(0,0,0), model="cube", texture="white_cube", color=color.white, highlight=color.lime):
        super().__init__(
            parent = ursina.scene,
            position = position,
            model = model,
            origin_y = 0.5,
            texture = texture,
            color = color,
            highlight_color = highlight
        )
    
    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                voxel = Voxel(
                    position = self.position + mouse.normal
                )
        
            elif key == "left mouse down":
                destroy(self)