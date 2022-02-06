from random import randint, randrange
import random
from tracemalloc import start

class Individual:
    def __init__(self)->None:
        self.genome = ''
        self.score = 0
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score

# Generating the inicial population
def generate_initial_population(population_size, population, cities_quantity, cities_distance_matrix):
    individual = Individual()
    for _ in range(population_size):
        individual = Individual()
        individual.genome = generate_genome(0, cities_quantity)
        individual.score = calculate_score(individual.genome, cities_distance_matrix)
        population.append(individual)
    return population

# Generates a random genome witou repeating cities
def generate_genome(initial: int, cities_quantity = 5) -> str:
    genome = list(range(cities_quantity))
    genome.remove(initial)
    
    random.shuffle(genome)
    genome.insert(0, initial)
    genome = ''.join([str(s) for s in genome])
    
    return genome

# Check if the string repeat a city
def if_city_in_genoma(genome, city):
    for i in genome:
        if i == city:
            return True
    return False

# Calculate the score of the path defined by the gene
def calculate_score(genome, cities_distance_matrix):
    path_size = 0
    for i in range(len(genome)-1):
        path_size += cities_distance_matrix[int(genome[i])][int(genome[i+1])]
    return path_size


# Swap genome value
def swap_genome(genome,cities_quantity, probability = 0.5):
    if randrange(0,1) <=probability:
        genome = list(genome)
        while True:
            position1 = randint(1, cities_quantity-1)
            position2 = randint(1, cities_quantity-1)
            if position1 != position2:
                #swap for 2 variables
                genome[position1], genome[position2]    = genome[position2], genome[position1]
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
        cities_quantity = int(input())

        print("Tamanho da população inicial:")
        population_size = int(input())

        print("Quantidade de gerações:")
        generations_quantity = int(input())

        cities_distance_matrix =[]
        print("matriz distancia das cidades")
        for i in range(cities_quantity):
            cities_distance_matrix.append(list(map(int, input().split())))
    else:
        cities_quantity = 5
        generations_quantity = 100
        population_size = 10
        cities_distance_matrix=[
                    [0, 2, 3, 12, 5],
                    [2, 0, 4, 8, 4],
                    [17, 4, 0, 3, 3],
                    [12, 8, 3, 0, 10],
                    [5, 5, 3, 10, 0],
            ]

    population = []
    population = generate_initial_population(population_size, population, cities_quantity, cities_distance_matrix)

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
            temp_genome.genome = swap_genome(population[i].genome, cities_quantity)
            temp_genome.score = calculate_score(temp_genome.genome, cities_distance_matrix)
            population.append(temp_genome)
        population.sort()

        #elitist selection
        population = elitist_selection(population, population_size)
    
    print("Final population = individual score")
    for i in range(len(population)):
        print(str(i) +" "+ population[i].genome + ' ' + str(population[i].score))