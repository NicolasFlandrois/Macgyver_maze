#!usr/bin/python3
#Tue 15 Jan 2019 05:03:37 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import os

#newmaze_name = "newmaze_" + input("mazenumber? ") #How can I Automate this?
TARGET_DIR = './maze_board/'
n = sum(1 for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)))
new_name = "{}maze_{}.txt".format(TARGET_DIR,n+1)

with open(new_name, 'w') as newmaze:
		
	lst = []
	length = int(input("How many tiles your maze's length will be? "))
	filler = 0

	for i in range(length**2):
		lst.append(filler)
	
	row_len = int(sqrt(len(lst))) + 1
	border_row_len = row_len + 1
	maze_view = []

	for pos in enumerate(lst):
		if ((float(pos[0]) + row_len)%row_len) == 0:
			lst.insert(int(pos[0]), '8')

	for i in range(border_row_len-1):
		lst.append('8')

	for pos in enumerate(lst):
		if ((float(pos[0]) + border_row_len)%border_row_len) == 0:
			lst.insert(int(pos[0]), '\n')
	
	maze_view = " ".join([str(i) for i in lst])
	newmaze.write(maze_view)
	print(newmaze)
	print("Finished process")

#Still to do:
# > During creation, consider:
#		- length input = maze's size. Free space that player will play in.
#		- fill automatically with borders, so far = 8; 
#			either fill it on the right or left, depends which is easier.