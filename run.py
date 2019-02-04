#!usr/bin/python3.6
#UTF8
#Date: 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import pygame as pg
from sys import exit
from random import randrange as randrange

#Immuable/Initial variables
#white = (255,255,255)
#black = (0,0,0)	
state = "run"
count = 3

#Game play
if __name__ == '__main__':
		game = Game()
		maze = Maze()
		game.main(maze, maze.get_row_length())