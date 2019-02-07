from maze import Maze
import pygame as pg


class Game():
    """docstring for Game"""
    def __init__(self):
        pg.init()
        self.WHITE = (255, 255, 255)
        self.maze = Maze("./levels/001.txt")
        self.state = "run"
        self.font = pg.font.Font("./media/arial.ttf", 20)
        self.remain0 = self.font.render(
            "Remaining components : 0", True, self.WHITE)
        self.remain1 = self.font.render(
            "Remaining components : 1", True, self.WHITE)
        self.remain2 = self.font.render(
            "Remaining components : 2", True, self.WHITE)
        self.remain3 = self.font.render(
            "Remaining components : 3", True, self.WHITE)
        self.txtlose = self.font.render(
            "You lost. Try Again!", True, self.WHITE)
        self.txtwin = self.font.render("WINNER !", True, self.WHITE)
        WIDTH = self.maze.row_len*30
        HEIGHT = self.maze.row_len*30 + 30
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # loading TEXTURES
        self.TEXTURES = {i: pg.image.load(
            "./media/{}.png".format(i)) for i in range(1, 7)}

    def resolve(self):
        """This function will define a win/lose situation"""
        # Check if there is a guardian, and define if win or lose
        if not self.maze.has_guardian():
            self.state = "win" if self.maze.components_count == 0 else "lose"

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear Screen (fill screen with black)
        self.maze.draw(self.TEXTURES, self.screen)
        remain_text = None
        # Rendering count of remaining components to pick up
        if self.maze.components_count == 0:
            remain_text = self.remain0
        elif self.maze.components_count == 1:
            remain_text = self.remain1
        elif self.maze.components_count == 2:
            remain_text = self.remain2
        else:
            remain_text = self.remain3
        self.screen.blit(remain_text, (
            0, self.screen.get_height() - remain_text.get_rect().height))
        # Rendering win/lose text on screen, according to state status
        # (run, win, lose)
        if self.state == "lose":
            self.screen.blit(self.txtlose, (
                self.screen.get_width()/2 - self.txtlose.get_rect().width/2,
                self.screen.get_height()/2 - self.txtlose.get_rect().height/2))
        elif self.state == "win":
            self.screen.blit(self.txtwin, (
                self.screen.get_width()/2 - self.txtwin.get_rect().width/2,
                self.screen.get_height()/2 - self.txtwin.get_rect().height/2))
        pg.display.update()

    def run(self):
        """Main function for running this script in Pygame"""
        while True:
            self.draw()
            # Events Loop
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if self.state != "run":
                        exit()
                    else:
                        if event.key == pg.K_ESCAPE:
                            exit()
                        elif event.key in (
                                pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN):
                            self.maze.move_character(event.key, self.resolve)
