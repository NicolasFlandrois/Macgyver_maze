maze = []
with open("maze1.txt") as f:
	maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]
	print(maze)

#def maze_map():
#retranscrire la liste sous forme de tableau type maze1.txt
#changer la liste en string
#Effectuer un retour a la ligne tous les 5 caracteres
#Positioner des espace entre chaques caracteres
#>>> a = ['a', 'b', 'c', 'd']
#>>> ''.join(a)
#'abcd'

#While True:
	#u = up (position +1 row)
	#d = down (position (1 row)
	#r = right (position +1)
	#l = left (position -1)
	#q = quit the while infinit loop
	#All other keys = message d'erreur + rappel des keys
	#Attention ne pas depasser le 0 (en x ou y), lorsqu'il est sur les bordures du damier/maze, le joueur ne peux pas en sortir.

	#A chaques mouvements, ceci cree une nouvelle liste, qui remplace maze[]
	#A chaques mouvements, print maze en carre avec la fonction maze_map
	#5 fonctions
		# def mouvement()
		# def maze_map(): readable display
		# 
		#
		#
	#Respecter docstrings & PEP 8 (Max 80 caracteres pas lignes)

	#Rappel:
	#0 = Floor
	#1 = Wall (cannot go there)
	#2 = MacGyver (Player)
	#3 = Guardian
	#4 = Composents (ojets a trouver)

	#Question: comment creer une fonction editeur de maze, ne donnant qu'une string de zero?
	#Et la generation de maze, peut-il etre autonome et automatisé par python?