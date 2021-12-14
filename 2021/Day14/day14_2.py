#!/usr/bin/env python3

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

poly, rules = get_input()
steps = 40

count = {}
for i in range(len(poly) - 1):
    p = poly[i] + poly[i+1]
    if count.get(p, None) is None:
        count[p] = 1
    else:
        count[p] += 1

for _ in range(steps):
    p_step = [(k, v) for k, v in count.items()]
    cnt_step = {}
    for ps in p_step:
        p = ps[0][0] + rules.get(ps[0], None)
        if cnt_step.get(p, None) is None:
            cnt_step[p] = count[ps[0]]
        else:
            cnt_step[p] += count[ps[0]]
        p = rules.get(ps[0], None) + ps[0][1]
        if cnt_step.get(p, None) is None:
            cnt_step[p] = count[ps[0]]
        else:
            cnt_step[p] += count[ps[0]]
    count = cnt_step

letter_count = {poly[0]: 1}
for r in rules:
    if count.get(r, None) is not None:
        if letter_count.get(r[1], None) is not None:
            letter_count[r[1]] += count[r]
        else:
            letter_count[r[1]] = count[r]
print(letter_count)
least = min(letter_count, key = letter_count.get)
most = max(letter_count, key = letter_count.get)
print('part 2:', letter_count.get(most)-letter_count.get(least))
