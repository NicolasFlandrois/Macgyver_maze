class Maze():

	def __init__(self:list, path="./mazeboard/maze1.txt"):
		self.tiles = []
		with open(path) as f:
			self.tiles = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]


	def get_row_length(self:list):
		"""docstring"""
		return int(sqrt(len(self.tiles))) #Determine the length of a row from maze.


	def get_randomize_components(slef:list):
		"""Randomly assigning positions for antidote's components in maze. 
		This function needs to import random module"""
		for i in range(4,7): #For loop applied to components named (4, 5, 6)
			while True:
				rand_pos = randrange(len(slef)+1)
				if slef[rand_pos] == 0 :
					slef[rand_pos]= i
					break
				else:
					continue


	def draw(self:list, get_row_length:int):
		"""Rendering all graphics"""
		global state, count, remainct0, remainct1, remainct2
		global remaintxt, textwin, textlose

		screen = (pg.display.set_mode(((get_row_length*30), 
		(get_row_length*30)+remaintxt.get_rect().height))) #loading screen
		
		textures = {i: pg.image.load("./media/{}.png".format(i)) 
		for i in range(1,7)} #loading textures
		
		screen.fill(black) #Clear Screen (fill screen with black)	
		
		#Determine tiles' positions in pygame coordinates.
		for pos, tile in enumerate(slef):
			x = (pos%get_row_length)*30
			y = (pos//get_row_length)*30
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