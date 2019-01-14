#! bin/ python3
from math import sqrt as sqrt

#name = input("What is your Name? ")
#This variable will be used to timestamp and keep traces of various plays and duration to solve the maze. Like a Score records.
#format of this data base : Timestamp, Name, Maze#, DurationDelta(Timestamp @ Finish - Timestamp @ start)

maze = []
with open("maze1.txt") as f:
	maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]
	print(maze)

row_len = sqrt(len(maze))
#print(row_len) #test run command fro row length. Checked OK, it works.

def maze_view():
#retranscrire la liste sous forme de tableau type maze1.txt
#changer la liste en string = Ok, Done
	maze_view = "".join([str(i) for i in maze])
	print(maze_view)
#Effectuer un retour a la ligne tous les (row_leng) caracteres, utiliser une REGEX
#Positioner des espace entre chaques caracteres, REGEX?

maze_view()

#While True:
	#Current position of 2 (MacGyver/Player)
pos = maze.index(2)
#print(pos) # Test command
	#u = up (position +1 row)
	#d = down (position (1 row)
	#r = right (position +1)
	#l = left (position -1)
	#q = quit the while infinit loop
	#All other keys = message d'erreur + rappel des keys (make key input standard, Upper case or lower case doesn't matter)
	#Attention ne pas depasser le 0 (en x ou y), lorsqu'il est sur les bordures du damier/maze, le joueur ne peux pas en sortir.
	#If, Elif, Else
	#If 1 or X in new position = NO! Blocking player. No messages, player kept in place, ask for more instructions.
	#If 0, Then write 2 in new position, and replace old position by 0.

	#A chaques mouvements, ceci cree une nouvelle liste, qui remplace maze[]
	#A chaques mouvements, print maze en carre avec la fonction maze_map
	#5 fonctions
		# def mouvement()
		# def maze_map(): readable display
		# 
		#
		#
	#Respecter docstrings & PEP 8 (Max 80 caracteres pas lignes)
	
	#Display Scores, and time delta, who is the winner on this maze? Who won in shortest time?
	#Then Back in While loop, start a new game/maze/start over this maze  >>> Player Choose if he wants to Quite, Restart, or Start a new Maze.
	
	#Rappel:
	#0 = Floor
	#1 = Wall (cannot go there)
	#2 = MacGyver (Player)
	#3 = Guardian
	#4 = Composents (ojets a trouver)

	#Question: comment creer une fonction editeur de maze, ne donnant qu'une string de zero?
	#Et la generation de maze, peut-il etre autonome et automatise par python?
	#Comment lancer de la musique en meme temps que l'on joue? Utiliser la musique du generique de la serie, des annees 1980, en 8bits.
	
