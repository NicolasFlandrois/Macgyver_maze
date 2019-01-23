#!usr/bin/python3
#Wed 16 Jan 2019 12:49:54 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import pygame as pg
from sys import exit

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
		elif maze[pos-1] == 3:
			victory = True
			print("WINNER !")
		maze[pos-1] = 2
	elif direction in ("r", "right"):
		if (pos+1)%row_len == 0:
			return
		elif maze[pos+1] == 1:
			return
		elif maze[pos+1] == 3:
			victory = True
			print("WINNER !")
		maze[pos+1] = 2
	elif direction in ("u", "up"):
		if pos-row_len < 0:
			return
		elif maze[pos-row_len] == 1:
			return
		elif maze[pos-row_len] == 3:
			victory = True
			print("WINNER !")
		maze[pos-row_len] = 2
	elif direction in ("d", "down"):
		if pos+row_len >= len(maze):
			return
		elif maze[pos+row_len] == 1:
			return
		elif maze[pos+row_len] == 3:
			victory = True
			print("WINNER !")
		maze[pos+row_len] = 2
	else:
		return
	maze[pos] = 0


def main():
	pg.init()
	screen = pg.display.set_mode((500, 500))

	maze = []
	with open("maze_board/maze_1.txt") as f:
		maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]

	row_len = int(sqrt(len(maze)))
	victory = False
	textures = {i: pg.image.load("./media/{}.png".format(i)) for i in range(1,7)}
	print(textures)
	while True:
		screen.fill([0,0,0]) #Clear Screen

		for pos, tile in enumerate(maze):
			x = (pos%row_len)*30
			y = (pos//row_len)*30
			if tile != 0:
				screen.blit(textures[tile], (x, y))

		pg.display.update()

		for event in pg.event.get():
			print(event)
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

#		maze_view(maze, row_len)

		pos = maze.index(2)


if __name__ == '__main__':
	main()


#Respecter docstrings & PEP 8 (Max 79 caracteres per lines)
	
#Reminder:
#0 = Floor
#1 = Wall (cannot go there)
#2 = MacGyver (Player)
#3 = Guardian
#4 = Components (ojects to find)