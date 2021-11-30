#!/usr/bin/env python3
import re

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

def check_digits(val, count):
    pattern = '[0-9]{' + str(count) + '}'
    return bool(re.fullmatch(pattern, val))

def extract_int(string):
    return int(re.findall('[0-9]+', string)[0])

def check_height(string):
    pattern_cm = '[0-9]+cm'
    pattern_in = '[0-9]+in'
    if bool(re.fullmatch(pattern_cm, string)):
        hgt = extract_int(string)
        if 150 <= hgt <= 193:
            return True
    if bool(re.fullmatch(pattern_in, string)):
        hgt = extract_int(string)
        if 59 <= hgt <= 76:
            return True
    return False

data = get_input()
expflds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validators = {
        'byr': lambda x: check_digits(x, 4) and 1920 <= int(x) <= 2002,
        'iyr': lambda x: check_digits(x, 4) and 2010 <= int(x) <= 2020,
        'eyr': lambda x: check_digits(x, 4) and 2020 <= int(x) <= 2030,
        'hgt': lambda x: check_height(x),
        'hcl': lambda x: bool(re.fullmatch('#[0-9a-f]{6}', x)),
        'ecl': lambda x: bool(re.fullmatch('(amb|blu|brn|gry|grn|hzl|oth)', x)),
        'pid': lambda x: check_digits(x, 9)
        }
valid_passports = 0

for pp in data:
    is_valid = True
    for f in expflds:
        value = pp.get(f, None)
        try:
            if not validators[f](value):
                is_valid = False
                break
        except:
            is_valid = False
            break
    if is_valid:
        valid_passports += 1

print('Valid passports:', valid_passports)
