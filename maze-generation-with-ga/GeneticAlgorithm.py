from Maze import Maze

def fitness(maze: Maze):
    fit_value = 0
    max_path = maze.is_valid()
    
    if max_path == 0:
        fit_value -= 100
        
    fit_value += max_path * 2
    
    for line in maze.maze:
        for value in line:
            if value == 1:
                fit_value += 1
    
    return fit_value