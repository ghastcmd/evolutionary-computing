# dois gráficos:
# primeiro é quantidade de indivíduos únicos na população atual
# juntamente com quantidadede indivíduos únicos na população geral
# segundo é a média da população e o melhor indivíduo


import matplotlib.pyplot as plt
import numpy as np
import copy

from main import genetic_algorithm

def contains(val, norm_list):
    for it in norm_list:
        if val.genome == it.genome:
            return True
    return False

def remove_duplicate(population):
    for ind in population:
        if contains(ind, population):
            population[:] = list(
                filter(lambda a: a.genome != ind.genome, population)
            )

if __name__ == '__main__':
    cities_coordinates = [
        (1, 0),
        (23, -2),
        (11, -31),
        (-1, 5),
        (20, 20),
    ]
    
    num_generations = 5
    
    pop_list = genetic_algorithm(num_generations, 10, cities_coordinates, 2)
    
    
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
    
    print('Plotting the graphs...')

    X = []
    Y = []
    print(len(current))
    print(len(overall))
    for i, j in zip(current, overall):
        X.append(len(i))
        Y.append(len(j))
    
    plt.plot(range(1, num_generations+1), X, color='purple')
    plt.plot(range(1, num_generations+1), Y)
    plt.savefig('plot.png')
