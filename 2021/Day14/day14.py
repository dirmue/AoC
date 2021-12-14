#!/usr/bin/env python3
import collections

def get_input():
    tpl = ''
    rules = {}
    read_tpl = True
    with open('input.txt', 'r') as file:
        for line in file:
            if line.strip() == '':
                read_tpl = False
                continue
            if read_tpl:
                tpl = line.strip()
            else:
                pair, insert = line.strip().split(' -> ')
                rules[pair] = insert
    return tpl, rules

def build_polymer(tpl, rules):
    polymere = tpl[0]
    for i in range(len(tpl) - 1):
        polymere += rules.get(tpl[i]+tpl[i+1], '') + tpl[i+1]
    return polymere

poly, rules = get_input()
for i in range(10):
    poly = build_polymer(poly, rules)
count = collections.Counter(poly)
least = min(count, key = count.get)
most = max(count, key = count.get)
print('part 1:', count.get(most)-count.get(least))
