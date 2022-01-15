from GeneticAlgorithm import run

def get_levels(quantity: int = 2, step: int = 2):
   max_gen = quantity * step
   return run(100, 10, max_gen, 0.1, shape=(12, 48), quantity=quantity)

if __name__ == '__main__':
   mazes = get_levels(2)
      
   print('best mazes are:')
   print(f'The len of mazes: {len(mazes)}')
   # for maze in mazes:
   #    print(maze, '\n')