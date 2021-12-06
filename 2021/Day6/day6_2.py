#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data = list(map(lambda x : int(x), line.strip().split(',')))
    return data

def get_spawn_days(days, vstart, dstart=0):
    sday = vstart + dstart + 1
    result = []
    while sday <= days:
        result.append(sday)
        sday += 7 
    return result


data = get_input()
population = len(data)
num_days = 256
spawn_days = []
spawn_cnt = {}

for d in range(1, num_days + 1):
    spawn_cnt[d] = 0

for f in data:
    sd = get_spawn_days(num_days, f)
    for val in sd:
        if not val in spawn_days:
            spawn_days.append(val)
        spawn_cnt[val] += 1
    spawn_days.sort()

for nextd in spawn_days:
    sd = get_spawn_days(num_days, 8, nextd)
    print(sd)
    for val in sd:
        if not val in spawn_days:
            spawn_days.append(val)
        spawn_cnt[val] += spawn_cnt[nextd]
    population += spawn_cnt[nextd]
    spawn_days.sort()

print(population)
