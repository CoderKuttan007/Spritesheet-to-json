import json
import pygame
import sys

sprite_sheet = sys.argv[1]
tile_size = sys.argv[2]

class Sprite_sheet_to_json:
    def __init__(self, sprite_sheet, tile_size):
        self.sprite_sheet = pygame.image.load(sprite_sheet)
        self.tile_size = tile_size
        self.coords = []
        self.frame_count = 0
    
    def get_coords(self):
        x = 0
        y = 0

        width = self.sprite_sheet.get_width()
        height = self.sprite_sheet.get_height()

        rows = round(height // self.tile_size)
        cols = round(width // self.tile_size)
        
        for row in range(rows):
            y = self.tile_size * row
            for col in range(cols):
                x = self.tile_size * col
                coord = {"name": sprite_sheet.replace(".png", "") + "_" + str(self.frame_count + 1) , "coords": [x, y]}
                self.coords.append(coord)

        return self.coords

    def generate_json(self, sprite_sheet_name):
        sprite_sheet_json = open(sprite_sheet_name + ".json", 'w')
        self.coords = self.get_coords()
        
        sprite_sheet_data = json.dumps(self.coords, indent=4)
        sprite_sheet_json.write(sprite_sheet_data)

        sprite_sheet_json.close()

json_generator = Sprite_sheet_to_json(sprite_sheet, int(tile_size))
json_generator.generate_json(sprite_sheet.replace(".png", ""))