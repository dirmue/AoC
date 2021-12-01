#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(int(line))
    return data

data = get_input()
incr = 0
for i in range(2, len(data) - 1):
    incr += 1 if sum(data[i-1:i+2]) > sum(data[i-2:i+1]) else 0

print('increases: ', incr)
