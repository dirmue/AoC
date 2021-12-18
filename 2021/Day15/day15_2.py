#!/usr/bin/env python3
from math import sqrt, ceil

def get_input():
    data = []
    tile = []
    with open('input.txt', 'r') as file:
        for line in file:
            tile.append([int(x) for x in line.strip()])
    for l in tile:
        new_line = []
        for i in range(5):
            for r in l:
                r = r + i
                if r > 9:
                    r = r % 9
                new_line.append(r)
        data.append(new_line)
    tile = []
    for i in range(5):
        for l in data:
            new_line = []
            for r in l:
                r = r + i
                if r > 9:
                    r = r % 9
                new_line.append(r)
            tile.append(new_line)
    return tile

data = get_input()
max_x = len(data[0]) -1
max_y = len(data) - 1
f_values = {(0, 0): 0}
g_values = {(0, 0): 0}
pre = {(0, 0): None}
open_list = [(0, 0)]
closed_list = set()
found = False

def estimate(x, y,):
    return ceil(sqrt((max_x - x) ** 2 + (max_y - y) ** 2))

def get_neighbors(x, y):
    n = []
    for dx in [-1, 1]:
        if 0 <= x + dx <= max_x:
            n.append((x + dx, y))
    for dy in [-1, 1]:
        if 0 <= y + dy <= max_y:
            n.append((x, y + dy))
    return n

def expand_node(current_node):
    for n in get_neighbors(current_node[0], current_node[1]):
        if n in closed_list:
            continue
        tentative_g = g_values[current_node] + data[n[1]][n[0]]
        if n in open_list and tentative_g >= g_values[n]:
            continue
        pre[n] = current_node
        g_values[n] = tentative_g
        f_values[n] = tentative_g + estimate(n[0], n[1])
        if n not in open_list:
            open_list.append(n)

while len(open_list) > 0:
    current_node = open_list[0]
    open_list.remove(current_node)
    if current_node == (max_x, max_y):
        found = True
        break
    closed_list.add(current_node)
    expand_node(current_node)
    open_list.sort(key=lambda x: f_values[x])
    

if found:
    n = (max_x, max_y)
    path = [n]
    p = pre.get(n, None)
    while p is not None:
        path.append(p)
        n = p
        p = pre.get(n, None)
    risk = sum(list(map(lambda x: data[x[1]][x[0]], path)))
    print('part 2:', risk - data[0][0])
else:
    print('Path not found')
