import random

random.seed(1)

# Debug printing
DEBUG = False
def deb(*string, end='\n'):
    if DEBUG:
        print(*string, end=end)
        
def mutate(dna_string, prob=0.5):
    ret_str = dna_string.copy()
    
    prob_value = random.uniform(0,1)
    if prob_value < prob:
        index = random.choice(range(len(ret_str)))
        ret_str.insert(index, 'X')
    
    return ret_str

def more_mutate(dna, prob=0.5):
    ret_str = dna.copy()
    for i in range(len(ret_str)):
        prob_value = random.uniform(0,1)
        if prob_value < prob:
            dna.insert(i, 'X')
    
    return ret_str

def crossover(father_string, mother_string):
    idx = random.choice(range(min(len(father_string), len(mother_string))))
    return (father_string[:idx] + mother_string[idx:],
            mother_string[:idx] + father_string[idx:])

def equalize_strips(a, b, size):
    size_a = len(a)
    if size_a < size:
        diff = size - size_a
        for _ in range(diff):
            a.insert(size_a, 'X')
    
    size_b = len(b)
    if size_b < size:
        diff = size - size_b
        for _ in range(diff):
            b.insert(size_b, 'X')
    

# Weights are a = +1, b = 0, o = -1 \\
# 'a' are alignment with the same nitrogenated basis \\
# 'b' are alignment with different nitrogenated basis \\
# 'o' are alignment with gaps and nitrogenated basis \\
def score(string_a, string_b, max_size):
    score = 0
    
    first = string_a.copy()
    second = string_b.copy()
    
    equalize_strips(first, second, max_size)
    deb(first)
    deb(second)
    
    for a, b in zip(first, second):
        if a == 'X' or b == 'X':
            score += -1
            deb(' -1  ', end='')
        elif a == b:
            score += +1
            deb(' +1  ', end='')
        elif a != b:
            score +=  0
            deb(' +0  ', end='')
    deb('')
    return score

def permutate(values):
    ret_tuples = []
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            ret_tuples.append((i,j))
    return ret_tuples

def all_score(lists):
    perm = permutate(lists)
    
    max_size = 0
    for vv in lists:
        max_size = max(max_size, len(vv))
    
    ret_score_val = 0
    for val in perm:
        ret_score_val += score(lists[val[0]], lists[val[1]], max_size)
    
    return ret_score_val

def fitness(lists, orig_list):
    sum_score = all_score(lists)
    # Benefit the results that are smaller
    # list_max = 0
    # orig_max = 0
    # for list, orig in zip(lists, orig_list):
    #     list_max = max(list_max, len(list))
    #     orig_max = max(orig_max, len(orig))
    # lenght_penalty = list_max / orig_max

    # The weights must preferentially occur at
    # the middle of the sequence
    spacing_penalty = 0
    for val in lists:
        middle = len(val) / 2
        for i, vv in enumerate(val):
            if vv == 'X':
                spacing_penalty += abs(middle - i) / middle

    deb('==== weights ====')
    deb(sum_score, -spacing_penalty)

    return sum_score - spacing_penalty

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


SIMPLE_LIST1 = ['A', 'C', 'G', 'T', 'C', 'A']
SIMPLE_LIST2 = ['C', 'C', 'T', 'C']

ORIG_LIST = []
SOLUTIONS = []
NUM_GENERATIONS = 100

# def main():
#     seq = ['primeira', 'segunda', 'terceira', 'quarta', 'quinta']
#     for order in seq:
#         print(f"digite a {order} sequencia")
#         ORIG_LIST.append(list(map(str, input().split())))

def main():
    another = [
        'A C T C G T C',
        'A C T',
        'C G T C',
        'C G T',
        'T C G T A C'
    ]
    for value in another:
        ref_value = value.split(' ')
        
        ORIG_LIST.append(ref_value)

main()

for i in range(100):
    vals = []
    for i, val in enumerate(ORIG_LIST):
        new_string = mutate(val)
        vals.append(new_string)
        
    SOLUTIONS.append(vals)

for i in range(NUM_GENERATIONS):
    ranked_solutions = []
    
    for s in SOLUTIONS:
        ranked_solutions.append((fitness(s, ORIG_LIST), s))
    # print(ranked_solutions)
    
    ranked_solutions.sort()
    ranked_solutions.reverse()
    
    print(f'==== Gen {i} best solution ====')
    print(ranked_solutions[0])
    
    deb('===== the fitness =====')
    deb(fitness(ranked_solutions[0][1], ORIG_LIST))
    
    best_solutions = ranked_solutions[:10]
    
    elements = []
    for _ in range(100):
        first = random.choice(best_solutions)
        second = random.choice(best_solutions)
        
        children1 = []
        children2 = []
        
        for i, xy in enumerate(zip(first[1], second[1])):
            x, y = xy
            a, b = crossover_not_monster(x, y, ORIG_LIST, i)
            children1.append(mutate(a))
            children2.append(mutate(b))
        
        elements.append(children1)
        elements.append(children2)
    
    new_gen = []
    
    for val in best_solutions:
        new_gen.append(val[1])
    
    for _ in range(90):
        random_string = random.choice(elements)
        
        new_gen.append(random_string)
    
    for _ in range(10):
        random_string = random.choice(elements)
        
        values = []
        for val in random_string:
            values.append(more_mutate(val, 0.3))
        
        new_gen.append(values)
    
    SOLUTIONS = new_gen

# DEBUG = True
# fitness(SOLUTIONS[0], ORIG_LIST)