from random import randint, randrange
import copy
import random
import math

class Individual:
    def __init__(self)->None:
        self.genome = ''
        self.score = 0
        self.mutation_rate = 0
    
    def __str__(self):
        return f'{self.genome}'
    
    def __eq__(self, other):
        return self.genome == other.genome
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score

# Generating the inicial population
def generate_initial_population(population_size, cities_coordinates):
    population = []
    individual = Individual()
    cities_quantity = len(cities_coordinates)
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
def calculate_score(genome, cities_coordinates: list[tuple[int, int]]):
    path_size = 0
    for i in range(len(genome)-1):
        path_size += euclidean_distance(cities_coordinates[int(genome[i])], 
                                        cities_coordinates[int(genome[i+1])])
    return path_size


# Swap genome value
def swap_genome(genome: str, probability: float):
    genome = list(genome)
    for i in range(1, len(genome)):
        j = random.randint(1, len(genome)-1)
        if random.uniform(0, 1) < probability:
            genome[i], genome[j] = genome[j], genome[i]
    return ''.join(genome)

def hamming_distance(ind1: Individual, ind2: Individual) -> int:
    score = 0
    for a, b in zip(ind1.genome, ind2.genome):
        if a != b:
            score += 1
    score /= len(ind1.genome)
    return score

def crossover_muttrate(ind1: Individual, best: Individual, mut_rate: float):
    return (hamming_distance(ind1, best) * mut_rate + 0.01 + ind1.mutation_rate) / 2

def elitist_selection(population, elitist_number):
    new_population = population[:elitist_number]
    # for i in range(population_size):
    #     new_population.append(population[i])
    
    return new_population

def hamming_distance(ind1: Individual, ind2: Individual):
    score = 0
    str1 = list(ind1.genome)
    str2 = list(ind2.genome)
    for a, b in zip(str1, str2):
        if a != b:
            score += 1
    return score

def initialize_mutation_rates(population: list[Individual], max_mut_rate: float):
    min_max = population[-1].score - population[0].score
    min_score = population[0].score
    
    for ind in population:
        ind.mutation_rate = ((ind.score - min_score+1) / min_max) * max_mut_rate

# The function that runs the genetic algorithm
def genetic_algorithm(
    generations_quantity: int,
    population_size: int,
    cities_coordinates: list[tuple[int, int]],
    elitist_number: int,
    control = False,
    verbose: bool = False,
    init_pop: list = []
) -> list[list[Individual]]:
    cities_quantity = len(cities_coordinates)
    
    POPULATION_LIST = []
    
    population = []
    if init_pop == []:
        population = generate_initial_population(population_size, cities_coordinates)
    else:
        population = init_pop
    
    if control:
        population.sort()
        initialize_mutation_rates(population, 0.25)

    if verbose:
        print("Initial population | individual score")
        for i, ind in enumerate(population):
            if control:
                print(f'{i} {ind.genome} {ind.score} {ind.mutation_rate}')
            else:
                print(f'{i} {ind.genome} {ind.score}')

    for i in range(generations_quantity):
        population.sort()
        
        POPULATION_LIST.append(copy.deepcopy(population))
        
        if verbose:
            best = population[0]
            if control:
                print(f'==== Best Individual Gen# {i} ====\n{best.genome} {best.score} {best.mutation_rate}')
            else:
                print(f'==== Best Individual Gen# {i} ====\n{best.genome} {best.score}')
        
        #elitist selection
        population = elitist_selection(population, elitist_number)
        
        new_generation = []
        for i in range(population_size):
            temp_genome = Individual()
            rand_choice = random.choice(population)
            if control:
                best = population[0]
                temp_genome.genome = swap_genome(rand_choice.genome, rand_choice.mutation_rate)
                mut_rate = crossover_muttrate(rand_choice, best, 0.3)
                # temp_genome.genome = rand_choice_1.genome
                temp_genome.mutation_rate = mut_rate
            else:
                temp_genome.genome = swap_genome(rand_choice.genome, 0.25)
            temp_genome.score = calculate_score(temp_genome.genome, cities_coordinates)
            new_generation.append(temp_genome)

        population = new_generation

    print("Final population | individual score")
    for i, ind in enumerate(population):
        if control:
            print(f'{i} {ind.genome} {ind.score} {ind.mutation_rate}')
        else:
            print(f'{i} {ind.genome} {ind.score}')

    return POPULATION_LIST

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
        generations_quantity = 100
        cities_coordinates = [
            (1, 0),
            (23, -2),
            (11, -31),
            (-1, 5),
            (20, 20),
            # (1, 1),
            # (2, 3),
            # (-20, 1),
        ]
        population_size = len(cities_coordinates)
        # cities_distance_matrix=[
        #             [0, 2, 3, 12, 5],
        #             [2, 0, 4, 8, 4],
        #             [17, 4, 0, 3, 3],
        #             [12, 8, 3, 0, 10],
        #             [5, 5, 3, 10, 0],
        #     ]
        elitist_number = len(cities_coordinates) - len(cities_coordinates) // 3

    genetic_algorithm(
        generations_quantity, population_size,
        cities_coordinates, elitist_number, True, verbose
    )