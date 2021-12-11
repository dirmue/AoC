#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

data = get_input()
xlen = len(data[0])
ylen = len(data)
elevels = []
flashed = set()
num_flashes = 0

def flash(x, y):
    if (x, y) not in flashed:
        flashed.add((x, y))
        nflashes = 1
        neigh_flashes = set()
        for dx in [-1, 0 , 1]:
            if x + dx < 0 or x + dx > xlen - 1:
                continue
            for dy in [-1, 0, 1]:
                if y + dy < 0 or y + dy > ylen - 1 or (dx == 0 and dy == 0):
                    continue
                elevels[y+dy][x+dx] += 1
                if elevels[y+dy][x+dx] > 9:
                    neigh_flashes.add((x + dx, y + dy))
        for n_coords in neigh_flashes:
            nflashes += flash(n_coords[0], n_coords[1])
        return nflashes
    return 0

def step():
    for y in range(ylen):
        for x in range(xlen):
            elevels[y][x] += 1
    nflashes = 0
    for y in range(ylen):
        for x in range(xlen):
            if elevels[y][x] > 9:
                nflashes += flash(x, y)
    for f in flashed:
        elevels[f[1]][f[0]] = 0
    return nflashes


for y, line in enumerate(data):
    elevels.append([])
    for ch in line:
        elevels[y].append(int(ch))

final_step = 0
while len(flashed) != 100:
    final_step += 1
    flashed = set()
    num_flashes += step()
print('Part 2: Synchronized at step', final_step, ':-)')
