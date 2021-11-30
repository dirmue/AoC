#!/usr/bin/env python3

def get_input():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            split_list = line.split()
            char = split_list[1][0]
            min_cnt, max_cnt = split_list[0].split('-')
            passwd = split_list[2]
            data.append({
                'char': char, 
                'minc': int(min_cnt), 
                'maxc': int(max_cnt), 
                'pass': passwd})
    return data

def verify(pw_data):
    count = len(list(filter(lambda x: x == pw_data['char'], pw_data['pass'])))
    if pw_data['minc'] <= count <= pw_data['maxc']:
        return 1
    return 0

valid_passwords = 0

for pw in get_input():
    valid_passwords += verify(pw)
print(valid_passwords)
