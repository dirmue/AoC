#!/usr/bin/env python3
def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data


all_basins = []
covered = []
data = get_input()
lmax = len(data)
dmax = len(data[0])
vdata = [''] * dmax
risk_levels = 0

#find all low points
for lindex, line in enumerate(data):
    for dindex, digit in enumerate(line):
        vdata[dindex] += digit
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
            all_basins.append({
                'lowpoint': (dindex, lindex),
                'values': [data[lindex][dindex]]})
            risk_levels += 1 + int(digit)
print('part 1:', risk_levels)


def get_points(xytuple, value, dx, dy):
    neighbors = []
    result = []
    if value < 9 and xytuple not in covered:
        result.append(value)
        covered.append(xytuple)
    else:
        return []
    x = xytuple[0]
    y = xytuple[1]
    if y - 1 >= 0 and dy != 1:
            if int(data[y-1][x]) >= value:
                result += get_points((x, y-1), int(data[y-1][x]), dx=0, dy=-1)
    if y + 1 < lmax and dy != -1:
            if int(data[y+1][x]) >= value:
                result += get_points((x, y+1), int(data[y+1][x]), dx=0, dy=+1)
    if x - 1 >= 0 and dx != 1:
            if int(data[y][x-1]) >= value:
                result += get_points((x-1, y), int(data[y][x-1]), dx=-1, dy=0)
    if x + 1 < dmax and dx != -1:
            if int(data[y][x+1]) >= value:
                result += get_points((x+1, y), int(data[y][x+1]), dx=+1, dy=0)
    return result

for b in all_basins:
    x, y = b['lowpoint'][0], b['lowpoint'][1]
    if x + 1 < dmax:
        b['values'] += get_points((x+1, y), int(data[y][x+1]), dx=1, dy=0)
    if x - 1 >= 0:
        b['values'] += get_points((x-1, y), int(data[y][x-1]), dx=-1, dy=0)
    if y + 1 < lmax:
        b['values'] += get_points((x, y+1), int(data[y+1][x]), dx=0, dy=1)
    if y - 1 >= 0:
        b['values'] += get_points((x, y-1), int(data[y-1][x]), dx=0, dy=-1)

all_basins = sorted(all_basins, key=lambda x: len(x['values']), reverse = True)
result = 1
for i in range(0, 3):
    result = result * len(all_basins[i]['values'])
print('part 2:', result)
