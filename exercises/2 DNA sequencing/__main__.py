# First we have to define the dna

import random

orig_list=[]

for i in range(5):
    print("digite a primeira sequencia")
    orig_list.append(list(map(str, input().split())))

simple_list1 = ['A', 'C', 'G', 'T', 'C', 'A']
simple_list2 = ['C', 'C', 'T', 'C', 'G']

# another = simple_list1, simple_list2

def mutate(dna_string):
    ret_str = dna_string.copy()
    index = random.choice(range(len(ret_str)))
    ret_str.insert(index, 'X')
    
    return ret_str

# mutate(simple_list1.copy())

def crossover(father_string, mother_string):
    idx = random.choice(range(min(len(father_string), len(mother_string))))
    return (father_string[:idx] + mother_string[idx:],
            mother_string[:idx] + father_string[idx:])

# a, b = crossover(simple_list1, simple_list2)
# print(a)
# print(b)

def score(first, second):
    score = 0
    for a, b in zip(first, second):
        if a == 'X' or b == 'X':
            score += 0
        elif a == b:
            score += 1
        elif a != b:
            score -= 1
    return score

# val = score(a, b)
# print(val)

def permutate(values):
    ret_tuples = []
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            ret_tuples.append((i,j))
    return ret_tuples

# lists = [a, b, simple_list1, simple_list2]
# permutate(lists)

# print('this is after the thing')

def all_score(lists):
    perm = permutate(lists)
    
    ret_score_val = 0
    for val in perm:
        ret_score_val += score(lists[val[0]], lists[val[1]])
    
    return ret_score_val

def fitness(lists, orig_list):
    sum_score = all_score(lists)
    list_max = 0
    orig_max = 0
    for list, orig in zip(lists, orig_list):
        list_max = max(list_max, len(list))
        orig_max = max(orig_max, len(orig))
    lenght_penalty = list_max / orig_max

    return sum_score - lenght_penalty / 2

# print('     ')

# all = all_score([a, b, simple_list1])
# print(a)
# print(b)
# print(simple_list1)
# print(all)

def is_monster(dna_string, original_dna_list, pos):
    index = 0
    for val in original_dna_list[pos]:
        while dna_string[index] == 'X':
            index += 1
        if val != dna_string[index]:
            return True
        index += 1
    
    return False

def crossover_not_monster(father, mother, original, pos):
    a, b = crossover(father, mother)
    while is_monster(a, original, pos) or is_monster(b, original, pos):
        a, b = crossover(father, mother)
    return a, b

def mutate_not_monster(val, orig_list, pos):
    new_specie = mutate(val)
    while is_monster(new_specie, orig_list, pos):
        new_specie = mutate(val)
    return new_specie
    
# res = is_monster(a, another)
# print(a, another)
# print(res)

solutions = []
orig_list = [simple_list1, simple_list2]
start_list = orig_list.copy()
solutions = []

for i in range(100):
    vals = []
    for i, val in enumerate(orig_list):
        new_string = mutate_not_monster(val, orig_list, i)
        vals.append(new_string)
        
    solutions.append(vals)

for i in range(100):
    ranked_solutions = []
    
    for s in solutions:
        ranked_solutions.append((fitness(s, orig_list), s))
    # print(ranked_solutions)
    
    ranked_solutions.sort()
    ranked_solutions.reverse()
    
    print(f'==== Gen {i} best solution ====')
    print(ranked_solutions[0])
    
    best_solutions = ranked_solutions[:10]
    
    elements = []
    for s in best_solutions:
        values = []
        children1 = []
        children2 = []
        for i, val in enumerate(s[1]):
            new_specie = mutate_not_monster(val, orig_list, i)
            values.append(new_specie)
        
            a, b = crossover_not_monster(new_specie, val, orig_list, i)
            children1.append(a)
            children2.append(b)
            
        elements.append(values)
        elements.append(children1)
        elements.append(children2)
    
    # print(elements)
    
    new_gen = []
    for _ in range(100):
        
        
        new_gen.append(random.choice(elements))
    
    solutions = new_gen