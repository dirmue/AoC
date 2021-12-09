#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

data = get_input()
lmax = len(data)
dmax = len(data[0])
risk_levels = 0

for lindex, line in enumerate(data):
    for dindex, digit in enumerate(line):
        conditions = []
        if dindex - 1 >= 0:
            conditions.append(digit < line[dindex-1])
        if dindex + 1 < dmax:
            conditions.append(digit < line[dindex+1])
        if lindex - 1 >= 0:
            conditions.append(digit < data[lindex-1][dindex])
        if lindex + 1 < lmax:
            conditions.append(digit < data[lindex+1][dindex])
        if all(conditions):
            risk_levels += 1 + int(digit)
print('overall risk level:', risk_levels)
