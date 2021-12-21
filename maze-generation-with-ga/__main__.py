class Maze:
    def __init__(
        self, 
        maze: list, 
        start: tuple = (0,0),
        end: tuple = (0,0)
    ):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])

        self.start_pos = (0,0)
        if start != (0,0):
            self.start_pos = start
        if end != (0,0):
            self.end_pos = end
        else:
            self.end_pos = (self.height//2, self.width-1)

    def color_points(self):
        self.maze[self.start_pos[0]][self.start_pos[1]] = -2
        self.maze[self.end_pos[0]][self.end_pos[1]] = -1

    def print_maze(self):
        for line in self.maze:
            print(line)

default_maze = Maze([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])

print(default_maze.width)
default_maze.color_points()
default_maze.print_maze()