# !usr/bin/python3.6
# UTF8
# Date: Thu 07 Feb 2019 04:22:15 PM CET
# Author: Nicolas Flandrois

from game import Game
import os

#Determining number of available levels
TARGET_DIR = './levels/'
n = sum(1 for f in os.listdir(TARGET_DIR) 
    if os.path.isfile(os.path.join(TARGET_DIR, f)))

# Game play
if __name__ == '__main__':
    #Processing levels one after an other
    for level in range(1, n+1):
        currentlevel = "{}{}.txt".format(TARGET_DIR,level)
        game = Game(currentlevel)
        game.run()
#How to continue from a level to another, without quitting the game?