import sys

import print_table
from copy import deepcopy
import situations as s

placed_com = 0
temppl = 0

class State(object):

    def __init__(self, board, next, parent, maxedpl, what_is_played):
        self._board = board
        self._next = []
        self._parent = parent
        self._maxedpl = maxedpl
        self._what_is_played = what_is_played


    def get_value(self, i):
        return self._board[i]


    def set_value(self, i, value):
        self._board[i] = value


    def valid_move(self, i, value):
        value = value.upper()
        if value not in "BW":
            return False

        return True


    def next_phase1(self):

        global placed_com
        global temppl
        for i in range(1,25):
            if self._board[str(i)] not in "BW":
                last = deepcopy(self._board)
                if self._maxedpl:
                    last[str(i)] = 'W'
                    # placed_com += 1
                    self._next.append(State(last, [], self, False, (str(i), 'W')))
                else:
                    last[str(i)] = 'B'
                    # temppl += 1
                    self._next.append(State(last, [], self, True, (str(i), 'B')))

        # for i in self._next:
        #     last = deepcopy(print_table.positions)
        #     print_table.positions[i._what_is_played[0]] = i._what_is_played[1]
        #
        #     print_table.table()
        #     print_table.positions = last


    def next_phase2(self):

        pl = ''
        if self._maxedpl:
            pl = 'W'
        else:
            pl = 'B'
        not_used = []
        my = []
        for i in self._board:
            if self._board[i] == pl:
                my.append(i)
            if self._board[i] not in "BW":
                not_used.append(i)

        possible_move = []
        for i in my:
            for j in s.blocked[i]:
                if self._board[j] not in "BW":
                    last = deepcopy(self._board)
                    last[j] = pl
                    last[i] = i
                    if pl == 'W':
                        self._next.append(State(last, [], self, False, (j, pl)))
                    else:
                        self._next.append(State(last, [], self, True, (j, pl)))


    def next_mill(self):

        opp = ''
        pl = ''
        if self._maxedpl:
            pl = 'W'
            opp = 'B'
        else:
            pl = 'B'
            opp = 'W'

        possible = []

        for i in self._board:
            if self._board[i] == opp:
                possible.append(i)

        # This part of code disables us to remove B if he has a morris too.
        op_morr = s.pos_of_morris(self, opp)
        if op_morr:
            possible.remove(op_morr[0][0])
            possible.remove(op_morr[0][1])
            possible.remove(op_morr[0][2])


        if possible:
            for i in possible:
                last = deepcopy(self._board)
                last[i] = i
                if pl == 'W':
                    self._next.append(State(last, [], self, False, (i, 'B')))
                else:
                    self._next.append(State(last, [], self, True, (i, 'W')))
        else:
            print("Cannot remove any player figure. ")


    def end(self):

        if s.all_closed(self, 'B') or s.number_of_pieces(self, 'B') < 3 :
            print("Computer wins")
            sys.exit()
        if s.all_closed(self, 'W') or s.number_of_pieces(self, 'W') < 3:
            print("Player wins")
            sys.exit()

        return

# sth = State(print_table.positions, [], None, False, None)
# print(s.number_of_pieces(sth, 'B'))
# used = []
# for i in s._board.values():
#     if i not in "BW":
#         used.append(i)
#
# print(used)
#
# in1 = input("fsdfds: ")
# print(type(in1))
# print(s._board)
# print(s.get_value('5'))
# print(s.set_value('5','B'))
# print(s.get_value('5'))
# print_table.table()
