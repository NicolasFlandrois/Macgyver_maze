#!usr/bin/python3.6
#Wed 16 Jan 2019 12:49:54 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import pygame as pg
from sys import exit
from random import randrange as randrange

def randomized_components(maze:list):
	"""This function randomly positions antidote components in maze. 
	This function needs to import random module"""
	for i in range(4,7): #For loop applied to components named (4, 5, 6)
		while True:
			rand_pos = randrange(len(maze)+1)
			if maze[rand_pos] == 0 :
				maze[rand_pos]= i
				break
			else:
				continue

def move(maze:list, direction:str, row_len:int):
	"""This function will define the player's moves, 
	and avoiding getting out of the maze's board, or colliding with walls"""
	pos = maze.index(2) #Catch player's position
	global victory
	if direction == pg.K_LEFT and pos%row_len != 0 and maze[pos-1] != 1:
		maze[pos-1] = 2
	elif (direction == pg.K_RIGHT and (pos+1)%row_len != 0 
		and maze[pos+1] != 1):
		maze[pos+1] = 2
	elif direction == pg.K_UP and pos-row_len > 0 and maze[pos-row_len] != 1:
		maze[pos-row_len] = 2
	elif (direction == pg.K_DOWN and pos+row_len < len(maze) 
		and maze[pos+row_len] != 1):
		maze[pos+row_len] = 2
	else:
		return
	maze[pos] = 0
	winlose(maze)

def winlose(maze:list):
	"""This function will define a win/lose situation"""
	#Count remaining components
	global state
	count = 0
	for n in maze:
		if n in (range(4,7)):
			count+=1
	#Check if there is a guardian, and define if win or lose
	if maze.count(3) != 0:
		pass
	else:
		if count != 0:
			state = "lose"
		else:
			state = "win"

def draw(maze:list, row_len:int):
	"""DOCSTRING HERE - Render graphics"""
	screen = pg.display.set_mode(((row_len*30), (row_len*30))) #load screen
	textures = {i: pg.image.load("./media/{}.png".format(i)) for i in range(1,7)} #load textures	
	global state
	global count
	screen.fill(black) #Clear Screen (fill screen with black)	
	#Tetermine tiles' position in pygame coordinates.
	for pos, tile in enumerate(maze):
		x = (pos%row_len)*30
		y = (pos//row_len)*30
		if tile != 0:
			screen.blit(textures[tile], (x, y)) 
	#Rendering win/lose text on screen, according to state status (run, win, lose)
	if state == "lose":
		text = pg.font.SysFont("Arial", 40).render("You lost. Try Again!", True, white)
		screen.blit(text, (screen.get_width()/2 - text.get_rect().width/2,
			screen.get_height()/2 - text.get_rect().height/2))			
	elif state == "win":
		text = pg.font.SysFont("Arial", 40).render("WINNER !", True, white)
		screen.blit(text, (screen.get_width()/2 - text.get_rect().width/2,
			screen.get_height()/2 - text.get_rect().height/2))

	pg.display.update()


def main(maze:list, row_len:int):
	"""Main function for running this script in Pygame"""
	pg.init()

	while True:
		global state
		draw(maze, row_len)
		#Events Loop
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if state != "run":
					exit()
				else:
					if event.key == pg.K_ESCAPE:
						exit()
					elif event.key in (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN):
						move(maze, event.key, row_len)

white = (255,255,255)
black = (0,0,0)	
state = "run"
#Import the maze from a .txt file, and convert it into a usable list.
maze = []
with open("maze_board/maze_1.txt") as f:
	maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]

row_len = int(sqrt(len(maze))) #Determine the length of a row from maze.
randomized_components(maze) #Randmonly positions components

if __name__ == '__main__':
		main(maze, row_len)