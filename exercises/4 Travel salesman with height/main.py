import random
import copy
import math


class Individual:
    def __init__(self) -> None:
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
        individual.score = calculate_score(
            individual.genome, cities_coordinates)
        population.append(individual)
    return population

# Generates a random genome witou repeating cities


def generate_genome(initial: int, cities_quantity=5) -> str:
    genome = list(range(cities_quantity))
    genome.remove(initial)

    random.shuffle(genome)
    genome.insert(0, initial)
    genome = ''.join([str(s) for s in genome])

    return genome


def euclidean_distance(point1: tuple[int], point2: tuple[int]):
    ret_value: float = 0
    counter = 0
    height_result = 0
    for i, j in zip(point1, point2):
        if counter <= 2:
            ret_value += (i - j) ** 2
        else:
            height_result = height_difference(i, j)
        counter += 1
    return math.sqrt(ret_value) + height_result


def height_difference(point1, point2):
    if point1 < point2:
        return point2 - point1
    return 0

# Calculate the score of the path defined by the gene


def calculate_score(genome, cities_coordinates: list[tuple[int, int]]):
    path_size = 0
    for i in range(len(genome)-1):
        path_size += euclidean_distance(cities_coordinates[int(genome[i])],
                                        cities_coordinates[int(genome[i+1])])
    return path_size

# Swap genome value


def crossover(genome: str, probability: float):
    genome = list(genome)
    for i in range(1, len(genome)):
        j = random.randint(1, len(genome)-1)
        if random.uniform(0, 1) < probability:
            genome[i], genome[j] = genome[j], genome[i]
    return ''.join(genome)


def elitist_selection(population, elitist_number):
    new_population = population[:elitist_number]

    return new_population


def crossover_muttrate(ind: Individual, best: Individual, worst: Individual, mut_rate: float):
    score_rate = (worst.score - best.score) / worst.score

    return (1 - score_rate) * mut_rate * ind.mutation_rate + mut_rate


def list_from_scores(ind_list: list[Individual]):
    vec_ret = []
    for ind in ind_list:
        vec_ret.append(ind.score - ind_list[0].score)
    return vec_ret


def mutation_rate_from_diversity(population: list[Individual]):
    best = population[0].score
    worst = population[-1].score
    return (1 - (worst - best) / worst)

# The function that runs the genetic algorithm


def genetic_algorithm(
    generations_quantity: int,
    population_size: int,
    cities_coordinates: list[tuple[int, int]],
    elitist_number: int,
    control=False,
    verbose: bool = True,
    init_pop: list = []
) -> list[list[Individual]]:
    POPULATION_LIST = []

    population = []
    if init_pop == []:
        population = generate_initial_population(
            population_size, cities_coordinates)
    else:
        population = init_pop

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
                print(
                    f'==== Best Individual Gen# {i} ====\n{best.genome} {best.score} {best.mutation_rate}')
            else:
                print(
                    f'==== Best Individual Gen# {i} ====\n{best.genome} {best.score}')

        # elitist selection
        population = elitist_selection(population, elitist_number)

        choice_weights = list_from_scores(population)
        choices = random.choices(
            population, choice_weights, k=population_size-2)
        new_generation = [population[0]]

        if control:
            mutation_rate = mutation_rate_from_diversity(population)

        # for i in range(population_size):
        for rand_choice in choices:
            temp_genome = Individual()
            # rand_choice = random.choices(population, choice_weights, k=1)[0]
            if control:
                temp_genome.genome = crossover(
                    rand_choice.genome, mutation_rate)
            else:
                temp_genome.genome = crossover(rand_choice.genome, 0.25)

            temp_genome.score = calculate_score(
                temp_genome.genome, cities_coordinates)
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
    # select the mode
    with_external_input = False
    verbose = True

    # Defining the initial values
    if with_external_input:

        print("Quantidade de cidades:")
        cities_quantity = int(input())

        print("Tamanho da população inicial:")
        population_size = int(input())

        print("Quantidade de gerações:")
        generations_quantity = int(input())

        print("Quantidade de elites:")
        elitist_number = int(input())

        print("É de controle? (1 - Verdadeiro ou 0 - Falso):")
        is_control = bool(input())

        cities_coordinates = []
        print("matriz distancia das cidades")
        for i in range(cities_quantity):
            cities_coordinates.append(list(map(int, input().split())))
    else:
        generations_quantity = 10
        cities_coordinates = [
            (1, 0, 3),
            (23, -2, 5),
            (11, -31, 7),
            (-1, 5, 2),
            (20, 20, 12),
        ]
        population_size = 6
        elitist_number = 3
        is_control = True

    genetic_algorithm(
        generations_quantity, population_size,
        cities_coordinates, elitist_number, is_control, verbose
    )
