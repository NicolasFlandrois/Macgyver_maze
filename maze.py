class Maze():

	def __init__(self, path="./mazeboard/maze1.txt"):
		self.tiles = []
		with open(path) as f:
			self.tiles = [int(n) for n in f.read().replace(" ", "").replace("\n", "")]


	def get_row_length(self):
		return int(sqrt(len(self.tiles))) #Determine the length of a row from maze.