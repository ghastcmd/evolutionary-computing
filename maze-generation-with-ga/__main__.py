from GeneticAlgorithm import run

if __name__ == '__main__':
   mazes = run(100, 10, 10, 0.1, shape=(12, 48), quantity=2)
      
   print('best mazes are:')
   print(f'The len of mazes: {len(mazes)}')
   # for maze in mazes:
   #    print(maze, '\n')