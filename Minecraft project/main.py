from ursina import*
import random
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

textures = {
    1: load_texture("minecraft_assets/Assets/Textures/Grass_Block.png"), 
    2: load_texture("minecraft_assets/Assets/Textures/Dirt_Block.png"), 
           3: load_texture("minecraft_assets/Assets/Textures/Brick_block.png"), 
           4: load_texture("minecraft_assets/Assets/Textures/Stone_Block.png"), 
           5: load_texture("minecraft_assets/Assets/Textures/Wood_Block.png")}


sky_texture = load_texture("minecraft_assets/Assets/Textures/Skybox.png")
walk_sound= Audio("minecraft_assets/Assets/SFX/Punch_Sound.wav")

window.exit_button.visible = False
block_pick = 1
blocks = []
jungle = []

class Block(Button):
    def __init__(self, position = (0, 0, 0), texture = textures[1]):
        super().__init__(parent = scene, 
                         position = position, 
                         model = "minecraft_assets/Assets/Models/Block", 
                         origin_y = 0.5, 
                         texture = texture, 
                         color = color.color(0, 0, 1), 
                         scale = 0.5)
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                walk_sound.play()
                new_block = Block(position = self.position + mouse.normal, texture = textures[1])
            elif key == 'right mouse down':
                walk_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(parent = scene, model = "sphere",
                         texture = sky_texture, 
                         scale = 150, 
                         double_sided = True)

class Tree(Entity):
    def __init__(self,position=(0,0,0)):
        super().__init__(parent = scene,
                        position = position,
                        model = "Assets/Models/low_poly_tree/Lowpoly_tree_sample.obj",
                        scale = (1, 1, 1))

def generate_trees(num_trees = 10, terrain_size = 15):
    for _ in range(num_trees):
        x = random.randint(0, terrain_size-1)
        y = 0.5
        z = random.randint(0, terrain_size-1)
        tree = Tree(position = (x, y ,z))
        jungle.append(tree)

def generate_terrain():
    for z in range(30):
        for x in range(30):
            height = random.randint(2, 10)
            block = Block(position=(x, height, z))
            blocks.append(block)

generate_terrain()
generate_trees()
fpc = FirstPersonController()
#sky = Sky()

for z in range(50):
    for x in range(50):
        block = Block(position=(x,0,z))

def update():
    global block_pick
    for i in range(1, 6):
        if held_keys[str(i)]:
            block_pick = i
            print(block_pick)
            break


    if held_keys["escape"]:
        application.quit()

app.run()