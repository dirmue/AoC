#!/usr/bin/env python3
from math import sqrt, ceil, floor

t_min_x = 88
t_max_x = 125
t_min_y = -157
t_max_y = -103

ycnt = 0
for x in range(0, 1000): # :-(
    for y in range(-1000, 1000): # :-(
        pos = [0, 0]
        step = 0
        while True:
            pos[0] += x - step if x - step > 0 else 0
            pos[1] += (y - step)
            if t_min_x <= pos[0] <= t_max_x and t_min_y <= pos[1] <= t_max_y:
                ycnt += 1
                break
            if pos[0] > t_max_x or pos[1] < t_min_y:
                break
            step += 1

print('Hit Count:', ycnt)
