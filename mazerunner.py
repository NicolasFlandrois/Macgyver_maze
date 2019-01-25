#!usr/bin/python3.6
#Wed 16 Jan 2019 12:49:54 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import pygame as pg
from sys import exit
from random import randrange as randrange

def maze_view(mylist:list, length:int):
	"""
	Maze_view intend to make the list more readable visually, and appealing.
	This function will display a list, 
	into a formated shape. The list is sliced and displayed according 
	to a given length.
		mylist = list we want to visualise.
		length = length of a row.
	"""
	list_view = ""
	for pos, tile in enumerate(mylist):
		path = ""
		if tile == 0 :
			path = " "
		elif tile == 1 :
			path = "#"
		elif tile == 2:
			path = "M"
		elif tile == 3:
			path = "G"
		else:
			path = str(tile)
		list_view+=path+" "
		if (pos + length+1)%length == 0:
			list_view+="\n"
	print(list_view)

def antidote(maze:list):
	"""This function position antidote components randomlyin maze. 
	This function needs random module"""
	for i in range(4,7):
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
	pos = maze.index(2)
	global victory
	if direction in ("l", "left"):
		if pos%row_len == 0:
			return
		elif maze[pos-1] == 1:
			return
		maze[pos-1] = 2
	elif direction in ("r", "right"):
		if (pos+1)%row_len == 0:
			return
		elif maze[pos+1] == 1:
			return
		maze[pos+1] = 2
	elif direction in ("u", "up"):
		if pos-row_len < 0:
			return
		elif maze[pos-row_len] == 1:
			return
		maze[pos-row_len] = 2
	elif direction in ("d", "down"):
		if pos+row_len >= len(maze):
			return
		elif maze[pos+row_len] == 1:
			return
		maze[pos+row_len] = 2
	else:
		return
	maze[pos] = 0

def main():
	"""Main function for running this script in Pygame"""
	pg.init()
	maze = []
	with open("maze_board/maze_1.txt") as f:
		maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]

	row_len = int(sqrt(len(maze)))
	antidote(maze)

	screen = pg.display.set_mode(((row_len*30), (row_len*30)))
	textures = {i: pg.image.load("./media/{}.png".format(i)) for i in range(1,7)}
	
	state = "run"

	while True:
		screen.fill([0,0,0]) #Clear Screen (fill screen with black)

		for pos, tile in enumerate(maze):
			x = (pos%row_len)*30
			y = (pos//row_len)*30
			if tile != 0:
				screen.blit(textures[tile], (x, y))

		pg.display.update()

		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					exit()
				elif event.key == pg.K_LEFT:
					move(maze, "l", row_len)
				elif event.key == pg.K_RIGHT:
					move(maze, "r", row_len)
				elif event.key == pg.K_UP:
					move(maze, "u", row_len)
				elif event.key == pg.K_DOWN:
					move(maze, "d", row_len)

		pos = maze.index(2)

		count = 0
		for n in maze:
			if n in (range(4,7)):
				count+=1
			pass

		if maze.count(3) != 0:
			continue
		else:
			if count != 0:
				state = "lose"
			else:
				state = "win"
			print(state) #run/win/lose statement
			exit()
			break
		
if __name__ == '__main__':
	main()

#Afficher a la fin du round (Gagner ou perdu), que le joueur a Gagner ou perdu >> Selon, faire apparaitre un texte dans Pygame, avec une Fonts

#Respecter docstrings & PEP 8 (Max 79 caracteres per lines)
	
#Reminder:
#0 = Floor
#1 = Wall (cannot go there)
#2 = MacGyver (Player)
#3 = Guardian
#Range(4,7) = Antidot Components (3 ojects to find)