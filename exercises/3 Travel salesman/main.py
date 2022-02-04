from random import randint, randrange
from tracemalloc import start
from turtle import position

class Individual:
  def __init__(self)->None:
    self.genome = ''
    self.score = 0
  def __lt__(self, other):
    return self.score < other.score
  def __gt__(self, other):
    return self.score > other.score

#Generating the inicial population
def generate_initial_population(population_size, population, citys_quantity, citys_distance_matrix):
  individual = Individual()
  for i in range(population_size):
    individual = Individual()
    individual.genome = generate_genome(citys_quantity)
    individual.score = calculate_score(individual.genome, citys_distance_matrix)
    population.append(individual)
  return population

#Generates a random genome witou repeating citys
def generate_genome(citys_quantity = 5):
  genome = '0'# defining the start city
  while len(genome) != citys_quantity:
    random_city = str(randint(1, (citys_quantity - 1)))
    if if_city_in_genoma(genome, random_city) == False:
      genome += random_city
  return genome

#check if the string repeat a city
def if_city_in_genoma(genome, city):
  for i in genome:
    if i == city:
      return True
  return False

#calculate the score of the path defined by the gene
def calculate_score(genome, citys_distance_matrix):
  path_size = 0
  for i in range(len(genome)-1):
    path_size += citys_distance_matrix[int(genome[i])][int(genome[i+1])]
  return path_size

# Generate new genomes based on iversion teory
# def invert_genome(genome,citys_quantity, probability = 0.5):
#   if randrange(0,1) <=probability:
#     while True:
#       genome_slice = []
#       genome_slice.append(randint(1, citys_quantity))
#       genome_slice.append(randint(1, citys_quantity))
#       if genome_slice[0] != genome_slice[1]:
#         break
#     genome_slice.sort()
    # value = genome[genome_slice[0]:genome_slice[1]]
    # value2 = genome[genome_slice[1]-1:genome_slice[0]-1:-1]

# swap genome value
def swap_genome(genome,citys_quantity, probability = 0.5):
  if randrange(0,1) <=probability:
    genome = list(genome)
    while True:
      position1 = randint(1, citys_quantity-1)
      position2 = randint(1, citys_quantity-1)
      if position1 != position2:
        #swap for 2 variables
        genome[position1], genome[position2]  = genome[position2], genome[position1]
        break
    return ''.join(genome)


def elitist_selection(population, population_size):
  new_population = []
  for i in range(population_size):
    new_population.append(population[i])
  return new_population
#Starting main
if __name__ == "__main__":

  #select the mode
  with_external_input = False
  verbose = False

  #Defining the initial values
  if with_external_input:

    print("Quantidade de cidades:")
    citys_quantity = int(input())

    print("Tamanho da população inicial:")
    population_size = int(input())

    print("Quantidade de gerações:")
    generations_quantity = int(input())

    citys_distance_matrix =[]
    print("matriz distancia das cidades")
    for i in range(citys_quantity):
      citys_distance_matrix.append(list(map(int, input().split())))
  else:
    citys_quantity = 5
    generations_quantity = 100
    population_size = 10
    citys_distance_matrix=[
          [0, 2, 3, 12, 5],
          [2, 0, 4, 8, 4],
          [17, 4, 0, 3, 3],
          [12, 8, 3, 0, 10],
          [5, 5, 3, 10, 0],
      ]

  population = []
  population = generate_initial_population(population_size, population, citys_quantity, citys_distance_matrix)

  if verbose:
    print("inicial population = individual score")
    for i in range(len(population)):
      print(str(i) +" "+ population[i].genome + ' ' + str(population[i].score))

  #generating mutations and evolving the population
  population.sort()
  for i in range(generations_quantity):
    if verbose:
      print("sorting result")
      for i in range(len(population)):
        print(str(i) +" "+ population[i].genome + ' ' + str(population[i].score))
    for i in range(population_size):
      temp_genome = Individual()
      temp_genome.genome = swap_genome(population[i].genome, citys_quantity)
      temp_genome.score = calculate_score(temp_genome.genome, citys_distance_matrix)
      population.append(temp_genome)
    population.sort()

    #elitist selection
    population = elitist_selection(population, population_size)
  
  print("Final population = individual score")
  for i in range(len(population)):
    print(str(i) +" "+ population[i].genome + ' ' + str(population[i].score))