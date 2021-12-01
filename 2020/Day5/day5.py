#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            data.append((line[:7], line[7:]))
    return data

data = get_input() 
ids = []

for seat in data:
    row = 0
    column = 0
    for i in range(7):
        if seat[0][i] == 'B':
            row |= 2 ** (6 - i)
    for i in range(3):
        if seat[1][i] == 'R':
            column |= 2 ** (2 - i)
    ids.append(row * 8 + column)
print('highest ID:', max(ids))

ids.sort()
for i in range(1, len(ids) - 1):
    if ids[i] - ids[i-1] == 2:
        print('my seat: ', ids[i] - 1)
