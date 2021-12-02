#!/usr/bin/env python3

def get_input():
    data = {}
    with open('input.txt', 'r') as file:
        for line in file:
            command = line.split()
            if data.get(command[0], None) is None:
                data[command[0]] = []
            data[command[0]].append(int(command[1]))
    return data

data = get_input()
hor_pos = sum(data['forward'])
depth = sum(data['down'])-sum(data['up'])
print('result:', hor_pos * depth)
