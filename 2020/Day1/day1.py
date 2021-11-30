#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(int(line))
    return data

data = get_input()

for i in range(len(data)):
    for j in range(len(data) - i):
        if data[i] + data[i+j] == 2020:
            print(data[i] * data[i+j])
