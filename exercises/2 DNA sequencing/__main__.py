# First we have to define the dna

import random
from itertools import permutations

simple_list1 = ['A', 'C', 'G', 'T', 'C', 'A']
simple_list2 = ['C', 'C', 'T', 'C', 'G']

another = simple_list1, simple_list2

def mutate(dna_string):
    ret_str = dna_string.copy()
    index = random.choice(range(len(ret_str)))
    ret_str.insert(index, 'X')
    
    return ret_str

mutate(simple_list1.copy())

def crossover(father_string, mother_string):
    idx = random.choice(range(min(len(father_string), len(mother_string))))
    return (father_string[:idx] + mother_string[idx:],
            mother_string[:idx] + father_string[idx:])

a, b = crossover(simple_list1, simple_list2)
print(a)
print(b)

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

val = score(a, b)
print(val)

def permutate(values):
    ret_tuples = []
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            ret_tuples.append((i,j))
    return ret_tuples

lists = [a, b, simple_list1, simple_list2]
permutate(lists)

print('this is after the thing')

def all_score(lists):
    perm = permutate(lists)
    
    ret_score_val = 0
    for val in perm:
        ret_score_val += score(lists[val[0]], lists[val[1]])
    
    return ret_score_val

print('     ')

all = all_score([a, b, simple_list1])
print(a)
print(b)
print(simple_list1)
print(all)

def detect_monster(dna_string, original_dna_list):
    string_copy = dna_string.copy()
    
    for i in reversed(range(len(string_copy))):
        if string_copy[i] == 'X':
            del string_copy[i]
    
    return not string_copy in original_dna_list

res = detect_monster(a, another)
print(a, another)
print(res)