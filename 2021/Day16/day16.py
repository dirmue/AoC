#!/usr/bin/env python3
from functools import reduce

def get_input():
    data = ''
    with open('input.txt', 'r') as file:
        for line in file:
            for ch in line.strip():
                data += '{0:04b}'.format(int(ch, 16))
    return data

def decode_literal(data):
    lit_len = 0
    lit_str = ''
    while True:
        more = data[0]
        lit_str += data[1:5]
        lit_len += 5
        if more == '0':
            break
        data = data[5:]
    literal = int(lit_str, 2)
    return lit_len, literal

def read_packet(data):
    if len(data) < 6:
        return None, data
    p_version = int(data[0:3], 2)
    p_type = int(data[3:6], 2)
    packet = {
            'version': p_version,
            'type': p_type,
            'literal': None,
            'subpackets': []
            }
    data = data[6:]
    if p_type == 4: # literal
        lit_len, packet['literal'] = decode_literal(data)
        data = data[lit_len:]
    else:           # operator
        l_type_id = int(data[0], 2)
        data = data[1:]
        if l_type_id == 0:
            sub_p_len = int(data[0:15], 2)
            sub_p_data = data[15:15+sub_p_len]
            data = data[15+sub_p_len:]
            while len(sub_p_data) > 6:
                sub_pk, sub_p_data = read_packet(sub_p_data)
                packet['subpackets'].append(sub_pk)
        else:
            sub_p_count = int(data[0:11], 2)
            data = data[11:]
            for _ in range(sub_p_count):
                sub_pk, data = read_packet(data)
                packet['subpackets'].append(sub_pk)
    return packet, data

def sum_versions(packet):
    version_sum = packet['version']
    for s_pk in packet['subpackets']:
        version_sum += sum_versions(s_pk)
    return version_sum

def calculate(packet):
    values = []
    for sp in packet['subpackets']:
        if sp['type'] == 4:
            values.append(sp['literal'])
        else:
            values.append(calculate(sp))
    if packet['type'] == 0:
        return sum(values)
    if packet['type'] == 1:
        return reduce(lambda x, y: x * y, values)
    if packet['type'] == 2:
        return min(values)
    if packet['type'] == 3:
        return max(values)
    if packet['type'] == 4:
        return packet['literal']
    if packet['type'] == 5:
        return 1 if values[0] > values[1] else 0
    if packet['type'] == 6:
        return 1 if values[0] < values[1] else 0
    if packet['type'] == 7:
        return 1 if values[0] == values[1] else 0

data = get_input()
parsed_packet, padding = read_packet(data)
print('Packet:', parsed_packet)
print('Padding:', padding)
print('Part 1:', sum_versions(parsed_packet))
print('Part 2:', calculate(parsed_packet))
