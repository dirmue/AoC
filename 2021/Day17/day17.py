#!/usr/bin/env python3
from math import sqrt, ceil, floor

t_min_x = 88
t_max_x = 125
t_min_y = -157
t_max_y = -103

def get_x_steps():
    minx = -0.5 + sqrt(0.25 + 2 * t_min_x)
    if minx < 0:
        minx = -0.5 - sqrt(0.25 + 2 * t_min_x)
    maxx = -0.5 + sqrt(0.25 + 2 * t_max_x)
    if maxx < 0:
        maxx = -0.5 - sqrt(0.25 + 2 * t_max_x)
    return ceil(minx), floor(maxx)


min_x_st, max_x_st = get_x_steps()
ymax = 0
for x in range(min_x_st, max_x_st):
    for y in range(0, 1000): # :-(
        pos = [0, 0]
        step = 0
        tmp_ymax = ymax
        while True:
            pos[0] += x - step if x - step > 0 else 0
            pos[1] += (y - step)
            if pos[1] > tmp_ymax: 
                tmp_ymax = pos[1]
            if t_min_x <= pos[0] <= t_max_x and t_min_y <= pos[1] <= t_max_y:
                if tmp_ymax > ymax: 
                    ymax = tmp_ymax
                break
            if pos[0] > t_max_x or pos[1] < t_min_y:
                break
            step += 1

print('Maximum Height:', ymax)
