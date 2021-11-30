#!/usr/bin/env python3

def get_input():
    data = []
    pp = {}
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip('\n')
            if line == '':
                data.append(pp)
                pp = {}
                continue
            fields = line.split()
            for f in fields:
                key, value = f.split(':')
                pp[key] = value
    if pp != {}:
        data.append(pp)
    return data

data = get_input()
expflds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0

for pp in data:
    is_valid = True
    for f in expflds:
        if pp.get(f, None) is None:
            is_valid = False        
    if is_valid:
        valid_passports += 1

print('Valid passports:', valid_passports)
