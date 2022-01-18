from MazeGeneration.GeneticAlgorithm import run

def get_levels(quantity: int = 2, step: int = 3):
   max_gen = quantity * step
   return run(110, 10, max_gen, 0.05, shape=(12, 48), quantity=quantity)

if __name__ == '__main__':
   mazes = get_levels(2)
   
   for maze in mazes:
      for line in maze:
         print(line)
      print("")
   
   # for maze in mazes:
   #    print(maze, '\n')
      
   print('best mazes are:')
   print(f'The len of mazes: {len(mazes)}')
   # for maze in mazes:
   #    print(maze, '\n')