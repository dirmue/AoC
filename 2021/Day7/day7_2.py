#!/usr/bin/env python3
from functools import reduce

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data = list(map(lambda x : int(x), line.strip().split(',')))
    return data

data = get_input()
min_pos = min(data)
max_pos = max(data)
fuel_cons = [] 
for pos in range(min_pos, max_pos + 1):
    fuel_cons.append(sum([reduce(lambda x, y: x + y, [x for x in range(0, max(d, pos) - min(d, pos) + 1)]) for d in data]))
        
print('Minimum fuel consumption:', min(fuel_cons))
