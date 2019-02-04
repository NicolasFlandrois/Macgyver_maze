class Maze():

	def __init__(self:list, path="./maze_board/maze_1.txt"):
		self.tiles = []
		with open(path) as f:
			self.tiles = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]


	def get_row_length(self:list):
		"""docstring"""
		return int(sqrt(len(self.tiles))) #Determine the length of a row from maze.


	def get_randomize_components(self:list):
		"""Randomly assigning positions for antidote's components in maze. 
		This function needs to import random module"""
		for i in range(4,7): #For loop applied to components named (4, 5, 6)
			while True:
				rand_pos = randrange(len(self.tiles)+1)
				if self.tiles[rand_pos] == 0 :
					self.tiles[rand_pos]= i
					break
				else:
					continue


	def draw(self:list, get_row_length:int):
		"""Rendering all graphics"""
		global state, count, #remainct0, remainct1, remainct2
		#global remaintxt, textwin, textlose

		screen = (pg.display.set_mode(((self.get_row_length()*30), 
		(self.get_row_length()*30)+game.render_text.remaintxt().get_rect().height))) #loading screen
		
		textures = {i: pg.image.load("./media/{}.png".format(i)) 
		for i in range(1,7)} #loading textures
		
		screen.fill(black) #Clear Screen (fill screen with black)	
		
		#Determine tiles' positions in pygame coordinates.
		for pos, tile in enumerate(self):
			x = (pos%self.get_row_length())*30
			y = (pos//self.get_row_length())*30
			if tile != 0:
				screen.blit(textures[tile], (x, y)) 
		
		#Rendering count of remaining components to pick up
		if count == 0:
			game.render_text.remaint() = game.render_text.remaint0()
		elif count == 1:
			game.render_text.remaint() = game.render_text.remaint1()
		elif count == 2:
			game.render_text.remaint() = game.render_text.remaint2()
		screen.blit(game.render_text.remaint(), (0, screen.get_height()- game.render_text.remaint().get_rect().height))
		
		#Rendering win/lose text on screen, according to state status (run, win, lose)
		if state == "lose":
			screen.blit(game.render_text.tlose(), (screen.get_width()/2 - game.render_text.tlose().get_rect().width/2, 
				screen.get_height()/2 - textlose.get_rect().height/2))			
		elif state == "win":
			screen.blit(game.render_text.twin(), (screen.get_width()/2 - game.render_text.twin().get_rect().width/2, 
				screen.get_height()/2 - game.render_text.twin().get_rect().height/2))

		pg.display.update()


#Test Lines
from math import sqrt as sqrt
import pygame as pg
from sys import exit
from random import randrange as randrange

maze = Maze()
game = Game()
print("test lines")
print("Row len : ", maze.get_row_length())
print(maze.get_randomize_components())
print(maze.draw(maze.get_row_length()))