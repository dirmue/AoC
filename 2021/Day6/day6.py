#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data = list(map(lambda x : int(x), line.strip().split(',')))
    return data

def fish_timer(x):
    if x > 0:
        return x - 1
    return 6

data = get_input()
zeroes = 0
num_days = 80

# too slow for part 2 :-(
for day in range (num_days):
    data = list(map(lambda x: fish_timer(x), data))
    data += zeroes * [8]
    print(f'Number of fish after day {day+1}: {len(data)}')
    zeroes = len(list(filter(lambda x: x == 0, data)))
