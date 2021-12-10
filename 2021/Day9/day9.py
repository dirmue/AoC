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
            all_basins.append({
                'lowpoint': (dindex, lindex),
                'values': []})
            risk_levels += 1 + int(digit)
print('part 1:', risk_levels)

# --- Part 2 ---

def get_points(xytuple, value):
    neighbors = []
    result = []
    if value < 9 and xytuple not in covered:
        result.append(value)
        covered.append(xytuple)
    else:
        return []
    x = xytuple[0]
    y = xytuple[1]
    if y - 1 >= 0 and (x, y - 1) not in covered:
            if int(data[y-1][x]) >= value:
                result += get_points((x, y-1), int(data[y-1][x]))
    if y + 1 < lmax and (x, y + 1) not in covered:
            if int(data[y+1][x]) >= value:
                result += get_points((x, y+1), int(data[y+1][x]))
    if x - 1 >= 0 and (x - 1, y) not in covered:
            if int(data[y][x-1]) >= value:
                result += get_points((x-1, y), int(data[y][x-1]))
    if x + 1 < dmax and (x + 1, y) not in covered:
            if int(data[y][x+1]) >= value:
                result += get_points((x+1, y), int(data[y][x+1]))
    return result

for b in all_basins:
    b['values'] += get_points(b['lowpoint'], int(data[b['lowpoint'][1]][b['lowpoint'][0]]))

all_basins = sorted(all_basins, key=lambda x: len(x['values']), reverse = True)
result = 1
for i in range(0, 3):
    result = result * len(all_basins[i]['values'])
print('part 2:', result)
