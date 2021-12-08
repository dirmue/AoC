#!/usr/bin/env python3

def get_input():
    in_val = []
    out_val = []
    with open('input.txt', 'r') as file:
        for line in file:
            in_val.append(line.strip().split(' | ')[0].split(' '))
            out_val.append(line.strip().split(' | ')[1].split(' '))
    return in_val, out_val

digits = {
    '0': None,
    '1': None,
    '2': None,
    '3': None,
    '4': None,
    '5': None,
    '6': None,
    '7': None,
    '8': set('abcdefg'),
    '9': None
    }


in_val, out_val = get_input()
results = []

for index, iv in enumerate(in_val):
    digits['1'] = set(list(filter(lambda x: len(x) == 2, iv))[0])
    digits['4'] = set(list(filter(lambda x: len(x) == 4, iv))[0])
    digits['7'] = set(list(filter(lambda x: len(x) == 3, iv))[0])
    seg_b_d = digits['1'] ^ digits['4']
    seg_e_g = (digits['7'] | digits['4']) ^ digits['8']
    seg_a = digits['7'] ^ digits['1']

    six_segments = list(filter(lambda x: len(x) == 6, iv))
    for d in six_segments:
        if len(set(d) & seg_b_d) == 1:
            digits['0'] = set(d)
        elif len(set(d) & seg_e_g) == 1:
            digits['9'] = set(d)
        else:
            digits['6'] = set(d)

    seg_e = digits['8'] ^ digits['9']
    seg_c = digits['8'] ^ digits['6']
    seg_b = digits['0'] & seg_b_d 
    seg_f = digits['1'] & digits['6']

    digits['5'] = digits['9'] ^ seg_c 
    digits['3'] = (digits['9'] ^ seg_b)
    digits['2'] = (digits['8'] ^ seg_b) ^ seg_f

    output = ''

    for ov in out_val[index]:
        for i in range(10):
            if set(ov) == digits.get(str(i)):
                output += str(i)
                break
    results.append(int(output))
print(sum(results))
