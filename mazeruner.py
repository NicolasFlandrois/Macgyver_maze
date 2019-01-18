#!usr/bin/python3
#Wed 16 Jan 2019 12:49:54 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt

name = input("What is your Name? ")
#This variable will be used to timestamp and keep traces of various plays and duration to solve the maze. Like a Score records.
#format of this data base : Timestamp, Name, Maze#, DurationDelta(Timestamp @ Finish - Timestamp @ start)

maze = []
with open("maze_board/maze_1.txt") as f:
	maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]
	print(maze)

row_len = int(sqrt(len(maze)))
print("row length: ", row_len) #test run command fro row length. Checked OK, it works.

def lstsqr_view(mylist:list, length:int):
	"""
	lstsqr_view stands for "List Square view", and intend to make a list 
	visually more readable. This function will display a list, 
	into a format shape. Each iteration of the list is separated by a space.
	Slices of the list are displaid according to a given length, in each line.
	
	Variables:
		mylist = list we want to visualise, type: list.
		length = length of a row, type: integer.
	"""
	list_view = []
	for pos in enumerate(mylist):
		if ((float(pos[0]) + length+1)%(length+1)) == 0:
			mylist.insert(int(pos[0]), '\n')
	list_view = " ".join([str(i) for i in mylist])
	print(list_view)
	for n in mylist:
		try:
			mylist.remove("\n")
		except ValueError:
			pass

while True:

	lstsqr_view(maze, row_len)

	pos = maze.index(2)
	print("player position, in cell: ", pos) # Test command
	print("Position coordinates: (", 
		int(pos%row_len), ",", 
		int(pos//row_len), ")")

	move = input("""
What is your next move?
	u = Up			l = Left
	d = Down		r = right

	q = quit
""").strip().lower()
	npos = pos
	if move in ("r", "right") :
		npos = int(pos) + 1 #r = right (position +1)
	elif move in ("l", "left") :
		npos = int(pos) - 1 #l = left (position -1)
	elif move in ("u", "up") :
		npos = int(pos) - row_len #u = up (position +1 row)
	elif move in ("d", "down") :
		npos = int(pos) + row_len #d = down (position -1 row)
	elif move in ("q", "quit", "exit") :
		break #q = quit the while infinit loop
	else:
		continue
	
	print("player New position, in cell: ", npos) #New position of 2 (MacGyver/Player) test command

	if maze[npos] not in (1, 8):
		maze[npos] = 2
		maze[pos] = 0
	else:
		continue

	print("maze list: ", maze) #reading test if \n remains

	#Respecter docstrings & PEP 8 (Max 80 caracteres pas lignes)
	
	#Display Scores, and time delta, who is the winner on this maze? Who won in shortest time?
	#Then Back in While loop, start a new game/maze/start over this maze  >>> Player Choose if he wants to Quite, Restart, or Start a new Maze.
	
	#Rappel:
	#0 = Floor
	#1 = Wall (cannot go there)
	#2 = MacGyver (Player)
	#3 = Guardian
	#4 = Composents (ojets a trouver)

	#Question: Comment lancer de la musique en meme temps que l'on joue? Utiliser la musique du generique de la serie, des annees 1980, en 8bits.
	
