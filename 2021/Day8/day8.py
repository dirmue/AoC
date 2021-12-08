#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data += line.strip().split(' | ')[1].split(' ')
    return data

data = get_input()
data = list(filter(lambda x: 2 <= len(x) <= 4 or len(x) == 7, data))
print('result: ', len(data))
