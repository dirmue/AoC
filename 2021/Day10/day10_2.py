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
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
        }
data = get_input()
scores = []
for line in data:
    chr_stack = []
    expected = []
    totalscore = 0
    for ch in line:
        try:
            if opening.get(ch, None) is not None:
                chr_stack.append(ch)
                expected.append(opening.get(ch, None))
            else:
                if chr_stack.pop() != closing.get(ch, None):
                    expected = []
                    break
                else:
                    expected.pop()
        except IndexError:
            expected = []
            break
    while len(expected) > 0:
        totalscore = totalscore * 5 + points[expected.pop()]
    if totalscore > 0:
        scores.append(totalscore)
scores.sort()
print('part 2:', scores[len(scores)//2])
