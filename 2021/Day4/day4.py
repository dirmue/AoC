#!/usr/bin/env python3

def get_input():
    rnd_num = []
    boards = []
    with open('input.txt', 'r') as file:
        rnd_num = file.readline().strip().split(',')
        rnd_num = list(map(lambda x: int(x), rnd_num))
        board_data = ''
        for line in file:
            board_data += line
        boards = [b.strip().split('\n') for b in board_data.split('\n\n')]
        for r in range(len(boards)):
            for c in range(len(boards[r])):
                boards[r][c] = boards[r][c].split()
                boards[r][c] = list(map(lambda x: int(x), boards[r][c]))
    return rnd_num, boards

class Board:

    def __init__(self, board_data):
        self._rows = board_data
        self._marked = []   # marked positions
        self._checked = []  # marked numbers

    def wins(self):
        rows = {}
        columns = {}
        for check in self._marked:
            if rows.get(check[0], None) is None:
                rows[check[0]] = 1
            else:
                rows[check[0]] += 1
                if rows[check[0]] == 5:
                    return True
            if columns.get(check[1], None) is None:
                columns[check[1]] = 1
            else:
                columns[check[1]] += 1
                if columns[check[1]] == 5:
                    return True
        return False

    def mark(self, number):
        if number in self._checked:
            return
        for r in range(len(self._rows)):
            for c in range(len(self._rows[r])):
                if number == self._rows[r][c]:
                    self._marked.append((r, c))
        self._checked.append(number) 

    def get_score(self, final_num):
        points = 0
        for r in self._rows:
            points += sum(list(filter(lambda x: x not in self._checked, r)))
        return points * final_num


class Game:

    def __init__(self, rnd_seq, boards):
        self._rnd_seq = rnd_seq
        self._boards = []
        for b in boards:
            self._boards.append(Board(b))

    def play(self):
        for num in self._rnd_seq:
            for b in self._boards:
                b.mark(num)
                if b.wins():
                    return b, b.get_score(num)

rnd_num, boards = get_input()
bingo = Game(rnd_num, boards)
first_score = 0
last_score = 0
while len(bingo._boards) > 0:
    b, last_score = bingo.play()
    if first_score == 0:
        first_score = last_score
    bingo._boards.remove(b)
print('First score (part 1):', first_score)
print('Last score (part 2):', last_score)
