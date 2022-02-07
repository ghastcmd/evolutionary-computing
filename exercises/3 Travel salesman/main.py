from random import randint, randrange
import random
import math

class Individual:
    def __init__(self)->None:
        self.genome = ''
        self.score = 0
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score

# Generating the inicial population
def generate_initial_population(population_size, population, cities_quantity, cities_coordinates):
    individual = Individual()
    for _ in range(population_size):
        individual = Individual()
        individual.genome = generate_genome(0, cities_quantity)
        individual.score = calculate_score(individual.genome, cities_coordinates)
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

def euclidean_distance(point1: tuple[int], point2: tuple[int]):
    ret_value: float = 0
    for i, j in zip(point1, point2):
        ret_value += (i - j) ** 2
    return math.sqrt(ret_value)


# Calculate the score of the path defined by the gene
def calculate_score(genome, cities_coodinates: list[tuple[int, int]]):
    path_size = 0
    for i in range(len(genome)-1):
        path_size += euclidean_distance(cities_coordinates[int(genome[i])], 
                                        cities_coordinates[int(genome[i+1])])
    return path_size


# Swap genome value
def swap_genome(genome,cities_quantity, probability = 0.5):
    if randrange(0,1) <=probability:
        genome = list(genome)
        while True:
            position1 = randint(1, cities_quantity-1)
            position2 = randint(1, cities_quantity-1)
            if position1 != position2:
                # Swap for 2 variables
                genome[position1], genome[position2]    = genome[position2], genome[position1]
                break
        return ''.join(genome)


def elitist_selection(population, elitist_number):
    new_population = population[:elitist_number]
    # for i in range(population_size):
    #     new_population.append(population[i])
    
    return new_population

# The function that runs the genetic algorithm
def genetic_algorithm(
    cities_quantity: int,
    generations_quantity: int,
    population_size: int,
    cities_coordinates: list[tuple[int, int]],
    elitist_number: int,
    verbose: bool = False
) -> list[list[Individual]]:
    POPULATION_LIST = []

    population = []
    population = generate_initial_population(population_size, population, cities_quantity, cities_coordinates)

    if verbose:
        print("Initial population | individual score")
        for i in range(len(population)):
            print(f'{i} {population[i].genome} {population[i].score}')

    for i in range(generations_quantity):
        population.sort()
        population.reverse()
        
        if verbose:
            print(f'==== Best Individual Gen# {i} ====\n{population[0].genome} {population[0].score}')
        
        #elitist selection
        population = elitist_selection(population, elitist_number)
        
        for i in range(population_size):
            temp_genome = Individual()
            rand_choice = random.choice(population)
            temp_genome.genome = swap_genome(rand_choice.genome, cities_quantity)
            temp_genome.score = calculate_score(temp_genome.genome, cities_coordinates)
            population.append(temp_genome)

    print("Final population | individual score")
    for i in range(len(population)):
        print(f'{i} {population[i].genome} {population[i].score}')


# Starting main
if __name__ == "__main__":
    #select the mode
    with_external_input = False
    verbose = True

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
        generations_quantity = 10
        population_size = 10
        cities_coordinates = [
            (1, 0),
            (23, -2),
            (11, -31),
            (-1, 5),
            (20, 20),
        ]
        # cities_distance_matrix=[
        #             [0, 2, 3, 12, 5],
        #             [2, 0, 4, 8, 4],
        #             [17, 4, 0, 3, 3],
        #             [12, 8, 3, 0, 10],
        #             [5, 5, 3, 10, 0],
        #     ]

    genetic_algorithm(
        cities_quantity, generations_quantity, population_size,
        cities_coordinates, population_size // 10, verbose
    )