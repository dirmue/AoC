#!/usr/bin/env python3

def get_input():
    data = []
    length = 0
    with open('input.txt', 'r') as file:
        for line in file:
            l = line.strip()
            if length < len(l):
                length = len(l)
            data.append(int(l, 2))
    return data, length

data, length = get_input()
ogr = data
co2sr = data

while len(ogr) > 1:
    for s in range(length, 0, -1):
        ones = list(filter(lambda x: (x >> (s - 1)) % 2 == 1, ogr))
        if len(ones) >= len(ogr) / 2:
            ogr = ones
        else:
            ogr = list(set(ogr) ^ set(ones))
        if len(ogr) == 1:
            break

while len(co2sr) > 1:
    for s in range(length, 0, -1):
        zeroes = list(filter(lambda x: (x >> (s - 1)) % 2 == 0, co2sr))
        if len(zeroes) <= len(co2sr) / 2 and len(zeroes) > 0:
            co2sr = zeroes
        else:
            co2sr = list(set(co2sr) ^ set(zeroes))
        if len(co2sr) == 1:
            break

print('ogr:', ogr[0])
print('co2sr:', co2sr[0])
print('support rating:', ogr[0] * co2sr[0])
