#!/usr/bin/env python3

def get_input():
    data = []
    length = 0
    with open('input.txt', 'r') as file:
        for line in file:
            l = line.strip()
            if length < len(l):
                length = len(l)
            data.append(int(l, 2))
    return data, length

data, length = get_input()
gamma = 0

for s in range(length):
    if len(list(filter(lambda x: x % 2 == 1, data))) >= len(data) / 2:
        gamma += 1 << s
    data = list(map(lambda x: x >> 1, data))
epsilon = 2 ** length - 1 - gamma
print('gamma rate:', gamma)
print('epsilon rate:', epsilon)
print('power consumption:', gamma * epsilon)
