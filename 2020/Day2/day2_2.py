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
                'pos1': int(min_cnt), 
                'pos2': int(max_cnt), 
                'pass': passwd})
    return data

def verify(pw_data):
    pw = pw_data['pass']
    if (pw[pw_data['pos1']-1] == pw_data['char']) ^ (pw[pw_data['pos2']-1] == pw_data['char']):
        return 1
    return 0

valid_passwords = 0

for pw in get_input():
    valid_passwords += verify(pw)
print(valid_passwords)
