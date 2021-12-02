#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            command = line.split()
            data.append((command[0], int(command[1])))
    return data

data = get_input()
aim = 0
hor_pos = 0
depth = 0

for c in data:
    if c[0] == 'up':
        aim -= c[1]
    if c[0] == 'down':
        aim += c[1]
    if c[0] == 'forward':
        hor_pos += c[1]
        depth += c[1] * aim

print('result:', hor_pos * depth)
