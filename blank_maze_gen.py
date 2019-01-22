#!usr/bin/python3
#Tue 15 Jan 2019 05:03:37 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import os

TARGET_DIR = './maze_board/'
n = sum(1 for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)))
new_name = "{}maze_{}.txt".format(TARGET_DIR,n+1)

with open(new_name, 'w') as newmaze:
		
	lst = []
	length = int(input("How many tiles your maze's length will be? "))

	for i in range(length**2):
		lst.append(0)
	
	row_len = int(sqrt(len(lst))) + 1
	maze_view = []

	for pos in enumerate(lst):
		if ((float(pos[0]) + row_len)%row_len) == 0:
			lst.insert(int(pos[0]), '\n')
	
	maze_view = " ".join([str(i) for i in lst])
	newmaze.write(maze_view)

	print("Finished process")