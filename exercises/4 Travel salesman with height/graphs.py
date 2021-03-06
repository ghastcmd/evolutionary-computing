# dois gráficos:
# primeiro é quantidade de indivíduos únicos na população atual
# juntamente com quantidadede indivíduos únicos na população geral
# segundo é a média da população e o melhor indivíduo


import matplotlib.pyplot as plt
import numpy as np
import copy
import random

from main import genetic_algorithm, generate_initial_population

def remove_duplicate(population):
    for ind in population:
        if ind in population:
            population[:] = list(
                filter(lambda a: a.genome != ind.genome, population)
            )
            population.append(ind)

def generate_graphics(pop_list: list, solutions_graph: str, solutions_graph_title: str, mean_graph: str, mean_graph_title: str):
    # This part is to make by each population
    current = copy.deepcopy(pop_list)    
    for pop in current:
        remove_duplicate(pop)
    
    # This part is to make accumulated population
    overall = []
    test_case = []
    for pop in pop_list:
        for ind in pop:
            test_case.append(ind)
        to_push = copy.deepcopy(test_case)
        remove_duplicate(to_push)
        overall.append(to_push)
    
    if test:
        print('Current')
        for pop in current:
            print(*pop, sep='\n')
            print('')
            
        print('Overall')
        for pop in overall:
            print(*pop, sep='\n')
            print('')
    
    print('Plotting the graphs...')

    # ! THIS PART IS FOR SOLUTIONS PER GENERATION
    current_lens = []
    overall_lens = []
    for cc, oo in zip(current, overall):
        current_lens.append(len(cc))
        overall_lens.append(len(oo))
    
    plt.clf()
    plt.plot(range(1, num_generations+1), current_lens, 
             color='purple', marker='o',
             label='Solutions per generation')
    plt.plot(range(1, num_generations+1), overall_lens, 
             color='green', marker='o',
             label='Overall solutions per generation')
    plt.title(solutions_graph_title)
    plt.legend(loc='best')
    plt.xlabel('Generation')
    plt.ylabel('Num. of Solutions')
    plt.savefig(solutions_graph)

    # ! THIS PART IS FOR MEAN AND BEST

    means_per_gen = []
    best_individual = []
    for pop in pop_list:
        mean = 0
        pop.sort()
        for ind in pop:
            mean += ind.score
        mean = mean / len(pop)
        means_per_gen.append(mean)
        best_individual.append(pop[0].score)
    
    plt.clf()
    plt.plot(range(1, num_generations+1), means_per_gen,
             color='blue', marker='v',
             label='Mean of score per generation')
    plt.plot(range(1, num_generations+1), best_individual,
             color='pink', marker='^',
             label='Score of the best individual of gen.')
    plt.title(mean_graph_title)
    plt.legend(loc='best')
    plt.xlabel('Generation')
    plt.ylabel('Score')
    plt.savefig(mean_graph)
    
    print('Finished plotting the graphs')

def generate_random_cities(num_cities: int, range_tuple: tuple[int, int]):
    cities = []
    
    for _ in range(num_cities):
        cities.append((
            random.randint(range_tuple[0], range_tuple[1]),
            random.randint(range_tuple[0], range_tuple[1]),
            random.randint(range_tuple[0]//2, range_tuple[1]//2)
        ))
    
    return cities

if __name__ == '__main__':
    # cities_coordinates = [
    #     (1, 0),
    #     (23, -2),
    #     (11, -31),
    #     (-1, 5),
    #     (20, 20),
    #     # (1, 1),
    #     # (2, 3),
    #     # (-20, 1),
    # ]
    
    cities_quantity = 6
    num_generations = 30
    population_size = 40
    elite_size = 10
    
    cities_coordinates = generate_random_cities(cities_quantity, (-20, 20))
    
    initial_population = generate_initial_population(population_size, cities_coordinates)
    
    pop_list = genetic_algorithm(num_generations, population_size, cities_coordinates, elite_size, control=True, init_pop=initial_population)
    
    print('Finished the Genetic Algorithm')
    
    test = False
    
    generate_graphics(
        pop_list,
        'solutions.png',
        'Quantity of solutions for each population per generation (with control)',
        'mean.png',
        'Mean and best individual per generation (with control)'
    )
