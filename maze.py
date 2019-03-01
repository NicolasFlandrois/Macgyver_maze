# !usr/bin/python3.6
# UTF8
# Date: Thu 07 Feb 2019 04:22:15 PM CET
# Author: Nicolas Flandrois

from math import sqrt as sqrt
from random import randrange as randrange


class Maze():
    """This class defines the components of the maze"""

    def __init__(self, path):
        self.tiles = []
        with open(path) as f:
            self.tiles = [
                int(n) for n in f.read().replace(" ", "").replace("\n", "")]
        self.randomize_components()
        self.row_len = int(sqrt(len(self.tiles)))
        self.components_count = 3
        self.UP = 273
        self.DOWN = 274
        self.RIGHT = 275
        self.LEFT = 276

    def randomize_components(self):
        """Randomly assigning positions for antidote's components in tiles.
        This function needs to import random module"""
        # For loop applied to components named (4, 5, 6)
        for i in range(4, 7):
            while True:
                rand_pos = randrange(len(self.tiles)+1)
                if self.tiles[rand_pos] == 0:
                    self.tiles[rand_pos] = i
                    break

    def update_components_count(self):
        """Counting remaining components"""
        self.components_count = 0
        for tile in self.tiles:
            if tile in range(4, 7):
                self.components_count += 1

    def has_guardian(self):
        """Checking if presence of a guardian"""
        return self.tiles.count(3) > 0

    def draw(self, textures, screen):
        """Rendering all graphics"""
        # Determine tiles' positions in pygame coordinates.
        for pos, tile in enumerate(self.tiles):
            x = (pos % self.row_len)*30
            y = (pos//self.row_len)*30
            if tile != 0:
                screen.blit(textures[tile], (x, y))

    def move_character(self, direction, game_resolution_function):
        """This function will define the player's moves,
        and avoiding getting out of the Maze's board, or colliding with walls
        """
        pos = self.tiles.index(2)  # Catch player's position
        if direction == self.LEFT and pos % self.row_len != 0 \
                and self.tiles[pos-1] != 1:
            self.tiles[pos-1] = 2
        elif direction == self.RIGHT and (pos+1) % self.row_len != 0 \
                and self.tiles[pos+1] != 1:
            self.tiles[pos+1] = 2
        elif direction == self.UP and pos-self.row_len > 0 \
                and self.tiles[pos-self.row_len] != 1:
            self.tiles[pos-self.row_len] = 2
        elif direction == self.DOWN and pos+self.row_len < len(self.tiles) \
                and self.tiles[pos+self.row_len] != 1:
            self.tiles[pos+self.row_len] = 2
        else:
            return
        self.tiles[pos] = 0
        self.update_components_count()
        game_resolution_function()
