#!usr/bin/python3.6
#UTF8
#Wed 16 Jan 2019 12:49:54 PM CET 
#Author: Nicolas Flandrois

from math import sqrt as sqrt
import pygame as pg
from sys import exit
from random import randrange as randrange

def randomize_components(maze:list):
    """Randomly assigning positions for antidote's components in maze. 
    This function needs to import random module"""
    for i in range(4,7): #For loop applied to components named (4, 5, 6)
        while True:
            rand_pos = randrange(len(maze)+1)
            if maze[rand_pos] == 0 :
                maze[rand_pos]= i
                break
            else:
                continue


def move(maze:list, direction:str, row_len:int):
    """This function will define the player's moves, 
    and avoiding getting out of the maze's board, or colliding with walls"""
    pos = maze.index(2) #Catch player's position
    if direction == pg.K_LEFT and pos%row_len != 0 and maze[pos-1] != 1:
        maze[pos-1] = 2
    elif (direction == pg.K_RIGHT and (pos+1)%row_len != 0 
        and maze[pos+1] != 1):
        maze[pos+1] = 2
    elif direction == pg.K_UP and pos-row_len > 0 and maze[pos-row_len] != 1:
        maze[pos-row_len] = 2
    elif (direction == pg.K_DOWN and pos+row_len < len(maze) 
        and maze[pos+row_len] != 1):
        maze[pos+row_len] = 2
    else:
        return
    maze[pos] = 0
    winlose(maze)


def winlose(maze:list):
    """This function will define a win/lose situation"""
    #Count remaining components
    global state, count
    count = 0
    for n in maze:
        if n in range(4, 7):
            count+=1
    #Check if there is a guardian, and define if win or lose
    if maze.count(3) == 0:
        state = "win" if count == 0 else "lose"


def draw(maze:list, row_len:int):
    """Rendering all graphics"""
    global state, count, remainct0, remainct1, remainct2
    global remaintxt, textwin, textlose

    screen = (pg.display.set_mode(((row_len*30), 
    (row_len*30)+remaintxt.get_rect().height))) #loading screen
    
    textures = {i: pg.image.load("./media/{}.png".format(i)) 
    for i in range(1,7)} #loading textures
    
    screen.fill(black) #Clear Screen (fill screen with black)   
    
    #Determine tiles' positions in pygame coordinates.
    for pos, tile in enumerate(maze):
        x = (pos%row_len)*30
        y = (pos//row_len)*30
        if tile != 0:
            screen.blit(textures[tile], (x, y)) 
    
    #Rendering count of remaining components to pick up
    if count == 0:
        remaintxt = remainct0
    elif count == 1:
        remaintxt = remainct1
    elif count == 2:
        remaintxt = remainct2
    screen.blit(remaintxt, (0, screen.get_height()- remaintxt.get_rect().height))
    
    #Rendering win/lose text on screen, according to state status (run, win, lose)
    if state == "lose":
        screen.blit(textlose, (screen.get_width()/2 - textlose.get_rect().width/2, 
            screen.get_height()/2 - textlose.get_rect().height/2))          
    elif state == "win":
        screen.blit(textwin, (screen.get_width()/2 - textwin.get_rect().width/2, 
            screen.get_height()/2 - textwin.get_rect().height/2))

    pg.display.update()


def main(maze:list, row_len:int):
    """Main function for running this script in Pygame"""
    pg.init()

    while True:
        global state
        draw(maze, row_len)
        #Events Loop
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if state != "run":
                    exit()
                else:
                    if event.key == pg.K_ESCAPE:
                        exit()
                    elif event.key in (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN):
                        move(maze, event.key, row_len)

#Immuable/Initial variables
white = (255,255,255)
black = (0,0,0) 
state = "run"
count = 3
#Import the maze from a maze_1.txt file, and convert it into a usable list.
maze = []
with open("./maze_board/maze_1.txt") as f:
    maze = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]

row_len = int(sqrt(len(maze))) #Determine the length of a row from maze.
randomize_components(maze) #Randmonly positions components
#Text to render further on, Components' countdown , Win, Lose
pg.font.init()
remainct0 = (pg.font.Font("./media/arial.ttf", 20)
    .render("Remaining components : 0", True, white))
remainct1 = (pg.font.Font("./media/arial.ttf", 20)
    .render("Remaining components : 1", True, white))
remainct2 = (pg.font.Font("./media/arial.ttf", 20)
    .render("Remaining components : 2", True, white))
remaintxt = (pg.font.Font("./media/arial.ttf", 20)
    .render("Remaining components : 3", True, white))
textlose = (pg.font.Font("./media/arial.ttf", 40)
    .render("You lost. Try Again!", True, white))
textwin = pg.font.Font("./media/arial.ttf", 40).render("WINNER !", True, white)
#Game play
if __name__ == '__main__':
        main(maze, row_len)