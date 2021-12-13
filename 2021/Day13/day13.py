#!/usr/bin/env python3
import re

def get_input():
    data = []
    fold_instr = []
    folds = False
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                folds = True
                continue
            if not folds:
                data.append(list(map(lambda x: int(x), line.split(','))))
            else:
                fold_instr += re.findall('[xy]=[0-9]+', line)
    return data, fold_instr

def fold(sheet, fold_instr):
    new_sheet = []
    direction = fold_instr.split('=')[0]
    f_border = int(fold_instr.split('=')[1])
    for p in sheet:
        if direction == 'x':
            if p[0] > f_border:
                p[0] = f_border * 2 - p[0]
        if direction == 'y':
            if p[1] > f_border:
                p[1] = f_border * 2 - p[1]
        if p not in new_sheet:
            new_sheet.append(p)
    return new_sheet



sheet, fold_instr = get_input()
folded = fold(sheet, fold_instr[0])
print(len(folded))
