from Ryan_Maluf.DFS.depth_first_search import dfs
from Ryan_Maluf.BFS.breadth_first_search import bfs


class Maze:
    def __init__(self, dim, obs):
        self.dim = dim
        self.obs = obs
        self.end = dim**2
        self.matrix = []

    def create_matrix(self):
        pass


maze = Maze(5, 30)
maze.create_matrix()
