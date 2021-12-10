#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

opening = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
        }

closing = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
        }

points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }
data = get_input()
pnts = 0
for line in data:
    chr_stack = []
    for ch in line:
        try:
            if opening.get(ch, None) is not None:
                chr_stack.append(ch)
            else:
                if chr_stack.pop() != closing.get(ch, None):
                    pnts += points.get(ch, 0)
        except IndexError:
            pnts += points.get(ch, 0)
print('part 1: ', pnts)
