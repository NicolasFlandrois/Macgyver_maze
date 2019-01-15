#! usr/bin/python3
#Tue 15 Jan 2019 05:03:37 PM CET 
from math import sqrt as sqrt

maze = []
for i in range(16**2):
	maze.append(0)
#print(maze)

row_len = sqrt(len(maze))
print("row length: ", row_len) #test run command fro row length. Checked OK, it works.

with open('newmaze.txt', 'a+') as newmaze:
#	maze = maze_view(maze)
	global row_len
	maze_view = []
	row_len+=1
	for pos in enumerate(maze):
		if ((float(pos[0]) + row_len)%row_len) == 0:
			maze.insert(int(pos[0]), '\n')
	maze_view = " ".join([str(i) for i in maze])
	newmaze.write(maze_view)