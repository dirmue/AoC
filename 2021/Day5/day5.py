#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            coords = line.strip().split(' -> ')
            coords = list(map(lambda x: x.split(','), coords))
            coords = list(map(lambda x: list(map(lambda y: int(y), x)), coords))
            data.append(coords)
    return data


class Line:

    def __init__(self, c):
        self.coords = {
                'x1': c[0][0],
                'y1': c[0][1],
                'x2': c[1][0],
                'y2': c[1][1]
                }

    def is_horizontal(self):
        return self.coords['y1'] == self.coords['y2']

    def is_vertical(self):
        return self.coords['x1'] == self.coords['x2']

    def is_diagonal(self):
        return abs((self.coords['x2'] - self.coords['x1']) / (self.coords['y2'] - self.coords['y1'])) == 1

    def get_points(self):
        p = []
        if self.is_vertical():
            y_min = min(self.coords['y1'], self.coords['y2'])
            y_max = max(self.coords['y1'], self.coords['y2'])
            y_coords = [y for y in range(y_min, y_max + 1)]
            p = list(zip([self.coords['x1']] * len(y_coords), y_coords))
        elif self.is_horizontal():
            x_min = min(self.coords['x1'], self.coords['x2'])
            x_max = max(self.coords['x1'], self.coords['x2'])
            x_coords = [x for x in range(x_min, x_max + 1)]
            p = list(zip(x_coords, [self.coords['y1']] * len(x_coords)))
        elif self.is_diagonal():
            x_step = -1 if self.coords['x1'] > self.coords['x2'] else 1
            y_step = -1 if self.coords['y1'] > self.coords['y2'] else 1
            x_coords = [x for x in range(self.coords['x1'], self.coords['x2'] + x_step, x_step)]
            y_coords = [y for y in range(self.coords['y1'], self.coords['y2'] + y_step, y_step)]
            p = list(zip(x_coords, y_coords))
        return p


coords = get_input()
lines = []
all_intersections = []
for c in coords:
    l = Line(c)
    # part 1: if l.is_horizontal() or l.is_vertical():
    if l.is_horizontal() or l.is_vertical() or l.is_diagonal():
        lines.append(l)

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        points_i = set(lines[i].get_points())
        points_j = set(lines[j].get_points())
        common = points_i & points_j
        for p in common:
            if p not in all_intersections:
                all_intersections.append(p)

print('\nsolution:', len(all_intersections))
