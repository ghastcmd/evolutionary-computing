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
    
    def generate_graph(self):
        graph = []
        
        for y, line in enumerate(self.maze):
            for x in range(len(line)):
                up = (y - 1) * self.width + x
                right = y * self.width + x + 1
                left = y * self.width + x - 1
                down = (y + 1) * self.width + x
                
                append_value = []
                              
                if y != 0:
                    append_value.append(up)
                
                if x != 0:
                    append_value.append(left)
                
                if y != self.height-1:
                    append_value.append(down)
                    
                if x != self.width-1:
                    append_value.append(right)
                
                graph.append(append_value)
        
        return graph

if __name__ == '__main__':

    test_maze = Maze([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])

    assert test_maze.width == 3
    assert test_maze.height == 3

    test_maze.color_points()
    assert test_maze.maze == [[-2, 0, 0], [0, 0, -1], [0, 0, 0]]

    graph = test_maze.generate_graph()

    assert graph == [[3, 1], [0, 4, 2], [1, 5], [0, 6, 4], [1, 3, 7, 5], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]