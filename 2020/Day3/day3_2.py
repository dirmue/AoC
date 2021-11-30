#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip('\n'))
    return data, len(data[0])

pattern, width = get_input()
lines = len(pattern)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1

for sl in slopes:
    trees = 0
    x, y = 0, 0
    x_stride = sl[0]
    y_stride = sl[1]

    while y + y_stride < lines:
        y += y_stride
        x = (x + x_stride) % width
        trees += 1 if pattern[y][x] == '#' else 0

    result = result * trees

print(result)
