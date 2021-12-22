from Maze import Maze
import random

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

def crossover(maze1: Maze, maze2: Maze):
    assert maze1.height == maze2.height
    assert maze1.width == maze2.width
    
    max_len = maze1.width * maze1.height
    point = random.choice(range(max_len))
    
    ret_maze1 = maze1.maze[:point] + maze2.maze[point:]
    ret_maze1 = Maze(ret_maze1)
    
    ret_maze2 = maze2.maze[:point] + maze1.maze[point:]
    ret_maze2 = Maze(ret_maze2)
    
    return (ret_maze1, ret_maze2)


if __name__ == '__main__':
    maze1 = Maze([[1,1], [1,1]])
    maze2 = Maze([[2,2], [2,2]])
    
    aaa1, aaa2 = crossover(maze1, maze2)
    print(aaa1)
    print(aaa2)