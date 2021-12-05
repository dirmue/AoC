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


    def is_identical(self, l):
        if self.m == l.m and self.b == l.b:
            return True
        return False

    def get_points(self, stepping=1):
        p = []
        if self.is_vertical():
            if self.coords['y1'] < self.coords['y2']:
                y = self.coords['y1']
                while y <= self.coords['y2']:
                    p.append((self.coords['x1'], y))
                    y += 1
            else:
                y = self.coords['y2']
                while y <= self.coords['y1']:
                    p.append((self.coords['x1'], y))
                    y += 1
        elif self.is_horizontal():
            if self.coords['x1'] < self.coords['x2']:
                x = self.coords['x1']
                while x <= self.coords['x2']:
                    p.append((x, self.coords['y1']))
                    x += 1
            else:
                x = self.coords['x2']
                while x <= self.coords['x1']:
                    p.append((x, self.coords['y1']))
                    x += 1
        elif self.is_diagonal():
            if self.coords['x1'] < self.coords['x2']:
                x = self.coords['x1']
                y = self.coords['y1']
                ystep = 1
                if y > self.coords['y2']:
                    ystep = -1
                while x <= self.coords['x2']:
                    p.append((x, y))
                    x += 1
                    y += ystep
            else:
                x = self.coords['x2']
                y = self.coords['y2']
                ystep = 1
                if y > self.coords['y1']:
                    ystep = -1
                while x <= self.coords['x1']:
                    p.append((x, y))
                    x += 1
                    y += ystep
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
                print('adding', p)
                all_intersections.append(p)

print('\nsolution:', len(all_intersections))
