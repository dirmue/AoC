#!/usr/bin/env python3
import re
from copy import copy

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

caves = {}
all_small_caves = set()
all_paths = []

def is_small(c):
    return c.islower()

def find_path(path=['start'], visited=set(), twice=''): 
    for next_cave in caves[path[len(path)-1]]:
        new_path = copy(path)
        v = copy(visited)
        if next_cave == 'end':
            new_path.append(next_cave)
            all_paths.append(new_path)
            continue
        if is_small(next_cave):
            if next_cave not in visited:
                v.add(next_cave)
                new_path.append(next_cave)
                find_path(new_path, v, twice)
            else:
                if next_cave == twice:
                    new_path.append(next_cave)
                    find_path(new_path, v, '')
        else:
            new_path.append(next_cave)
            find_path(new_path, v, twice)


data = get_input()
for l in data:
    c = l.split('-')
    if caves.get(c[0], None) == None and c[0] != 'end':
        caves[c[0]] = []
        if is_small(c[0]): all_small_caves.add(c[0])
    if caves.get(c[1], None) == None and c[1] != 'end':
        caves[c[1]] = []
        if is_small(c[1]): all_small_caves.add(c[1])
    if c[0] != 'end' and c[1] != 'start':
        caves[c[0]].append(c[1])
    if c[1] != 'end' and c[0] != 'start':
        caves[c[1]].append(c[0])

all_small_caves.remove('start')

for tw in all_small_caves:
    find_path(twice=tw)

result = set()
for p in all_paths:
    result.add(tuple(p))
print('part 2:', len(result))
