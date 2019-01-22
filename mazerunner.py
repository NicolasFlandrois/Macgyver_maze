#!usr/bin/python3
#Wed 16 Jan 2019 12:49:54 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt

maze = []
with open("maze_board/maze_1.txt") as f:
	maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]

row_len = int(sqrt(len(maze)))

def maze_view(mylist:list, length:int):
	"""
	Maze_view intend to make the list more readable visually, and appealing.
	This function will display a list, 
	into a formated shape. Each iteration of the list is separated by a space.
	The list is sliced and displayed according to a given length.
	
	Variables:
		mylist = list we want to visualise, type: list.
		length = length of a row, type: integer.
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

def move(maze:list, direction:str):
	"""This function will define the player's moves, 
	and avoiding getting out of the maze's board, or colliding with walls"""
	pos = maze.index(2)
	if direction in ("l", "left"):
		if pos%row_len == 0:
			return
		elif maze[pos-1] == 1:
			return
		elif maze[pos-1] == 3:
			run = "winner"
			print("WINNER !")
		maze[pos-1] = 2
	elif direction in ("r", "right"):
		if (pos+1)%row_len == 0:
			return
		elif maze[pos+1] == 1:
			return
		elif maze[pos+1] == 3:
			run = "winner"
			print("WINNER !")
		maze[pos+1] = 2
	elif direction in ("u", "up"):
		if pos-row_len < 0:
			return
		elif maze[pos-row_len] == 1:
			return
		elif maze[pos-row_len] == 3:
			run = "winner"
			print("WINNER !")
		maze[pos-row_len] = 2
	elif direction in ("d", "down"):
		if pos+row_len >= len(maze):
			return
		elif maze[pos+row_len] == 1:
			return
		elif maze[pos+row_len] == 3:
			run = "winner"
			print("WINNER !")
		maze[pos+row_len] = 2
	else:
		return
	maze[pos] = 0

run = "play"

while True:

	maze_view(maze, row_len)

	pos = maze.index(2)

	direction = input("""
What is your next move?
	u = Up			l = Left
	d = Down		r = Right

	q = quit
""").strip().lower()

	if direction in ("q", "quit", "exit") :
		break
	else:
		move(maze, direction)

	#Respecter docstrings & PEP 8 (Max 80 caracteres pas lignes)
	
	#Rappel:
	#0 = Floor
	#1 = Wall (cannot go there)
	#2 = MacGyver (Player)
	#3 = Guardian
	#4 = Components (ojects to find)