class Game(self):
	"""docstring for Game"""
	def __init__(self, Maze):
		super(Maze, self).__init__()
				

	def render_text(self):
		"""Text to render further on, Components' countdown , Win, Lose"""
		pg.font.init()
		remain0 = (pg.font.Font("./media/arial.ttf", 20)
			.render("Remaining components : 0", True, Maze.colors.white()))
		remain1 = (pg.font.Font("./media/arial.ttf", 20)
			.render("Remaining components : 1", True, Maze.colors.white()))
		remain2 = (pg.font.Font("./media/arial.ttf", 20)
			.render("Remaining components : 2", True, Maze.colors.white()))
		remain3 = (pg.font.Font("./media/arial.ttf", 20)
			.render("Remaining components : 3", True, Maze.colors.white()))
		txtlose = (pg.font.Font("./media/arial.ttf", 40)
			.render("You lost. Try Again!", True, Maze.colors.white()))
		txtwin = (pg.font.Font("./media/arial.ttf", 40)
			.render("WINNER !", True, Maze.colors.white()))


	def move(self, Maze:list, direction:str, get_row_length:int):
		"""This function will define the player's moves, 
		and avoiding getting out of the Maze's board, or colliding with walls"""
		pos = Maze.index(2) #Catch player's position
		if direction == pg.K_LEFT and pos%get_row_length != 0 and Maze[pos-1] != 1:
			Maze[pos-1] = 2
		elif (direction == pg.K_RIGHT and (pos+1)%get_row_length != 0 
			and Maze[pos+1] != 1):
			Maze[pos+1] = 2
		elif direction == pg.K_UP and pos-get_row_length > 0 and Maze[pos-get_row_length] != 1:
			Maze[pos-get_row_length] = 2
		elif (direction == pg.K_DOWN and pos+get_row_length < len(Maze) 
			and Maze[pos+get_row_length] != 1):
			Maze[pos+get_row_length] = 2
		else:
			return
		Maze[pos] = 0
		winlose(Maze)


	def winlose(self, Maze:list):
		"""This function will define a win/lose situation"""
		#Count remaining components
		global state, count
		count = 0
		for n in Maze:
			if n in range(4, 7):
				count+=1
		#Check if there is a guardian, and define if win or lose
		if Maze.count(3) == 0:
			state = "win" if count == 0 else "lose"


	def main(self, Maze:list, get_row_length:int):
		"""Main function for running this script in Pygame"""
		pg.init()

		while True:
			global state
			draw(Maze, get_row_length)
			#Events Loop
			for event in pg.event.get():
				if event.type == pg.KEYDOWN:
					if state != "run":
						exit()
					else:
						if event.key == pg.K_ESCAPE:
							exit()
						elif event.key in (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN):
							move(Maze, event.key, get_row_length)