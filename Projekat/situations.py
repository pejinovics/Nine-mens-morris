# Variation of situations in the game.
import state
import hashmap as h

blocked = h.LinearHashMap()
blocked['1'] = ('2', '10')
blocked['2'] = ('1', '3', '5')
blocked['3'] = ('2', '15')
blocked['4'] = ('11', '5')
blocked['5'] = ('2', '4', '6', '8')
blocked['6'] = ('5', '14')
blocked['7'] = ('8', '13')
blocked['8'] = ('5', '7', '9')
blocked['9'] = ('2', '10')
blocked['10'] = ('1', '11', '22')
blocked['11'] = ('4', '10', '12', '19')
blocked['12'] = ('7', '11', '16')
blocked['13'] = ('9', '18')
blocked['14'] = ('6', '13', '15', '21')
blocked['15'] = ('3', '14', '24')
blocked['16'] = ('12', '17')
blocked['17'] = ('16', '18', '20')
blocked['18'] = ('13', '17')
blocked['19'] = ('11', '20')
blocked['20'] = ('17', '19', '21', '23')
blocked['21'] = ('14', '20')
blocked['22'] = ('10', '23')
blocked['23'] = ('20', '22', '24')
blocked['24'] = ('15', '23')

coordinates1 = h.LinearHashMap()

coordinates1['1'] = ('1', 'a')
coordinates1['2'] = ('1', 'd')
coordinates1['3'] = ('1', 'g')
coordinates1['4'] = ('2', 'b')
coordinates1['5'] = ('2', 'd')
coordinates1['6'] = ('2', 'f')
coordinates1['7'] = ('3', 'c')
coordinates1['8'] = ('3', 'd')
coordinates1['9'] = ('3', 'e')
coordinates1['10'] = ('4', 'a')
coordinates1['11'] = ('4', 'b')
coordinates1['12'] = ('4', 'c')
coordinates1['13'] = ('4', 'e')
coordinates1['14'] = ('4', 'f')
coordinates1['15'] = ('4', 'g')
coordinates1['16'] = ('5', 'c')
coordinates1['17'] = ('5', 'd')
coordinates1['18'] = ('5', 'e')
coordinates1['19'] = ('6', 'b')
coordinates1['20'] = ('6', 'd')
coordinates1['21'] = ('6', 'f')
coordinates1['22'] = ('7', 'a')
coordinates1['23'] = ('7', 'd')
coordinates1['24'] = ('7', 'g')

coordinates = h.LinearHashMap()

coordinates[('1', 'a')] = '1'
coordinates[('1', 'd')] = '2'
coordinates[('1', 'g')] = '3'
coordinates[('2', 'b')] = '4'
coordinates[('2', 'd')] = '5'
coordinates[('2', 'f')] = '6'
coordinates[('3', 'c')] = '7'
coordinates[('3', 'd')] = '8'
coordinates[('3', 'e')] = '9'
coordinates[('4', 'a')] = '10'
coordinates[('4', 'b')] = '11'
coordinates[('4', 'c')] = '12'
coordinates[('4', 'e')] = '13'
coordinates[('4', 'f')] = '14'
coordinates[('4', 'g')] = '15'
coordinates[('5', 'c')] = '16'
coordinates[('5', 'd')] = '17'
coordinates[('5', 'e')] = '18'
coordinates[('6', 'b')] = '19'
coordinates[('6', 'd')] = '20'
coordinates[('6', 'f')] = '21'
coordinates[('7', 'a')] = '22'
coordinates[('7', 'd')] = '23'
coordinates[('7', 'g')] = '24'
# a = '5'
# b = 'd'
# tup = (a,b)
# print(coordinates[tup])
# for item in coordinates:
    # if coordinates[item] == tup:
    # print(item)
        # break

# Heuristics that I am using:
# 1. Closed Morris
# 2. Number of Morrises
# 3. Number of blocked opponent pieces
# 4. Number of pieces
# 5. Number of 2-piece configurations
# 6. Number of 3-piece configurations
# 7. Double morris
# 8. Winning configuration


# for each mill I use tuple as datatype because I won't change their values
mills = [('1', '2', '3'), ('1', '10', '22'), ('2', '5', '8'), ('3', '15', '24'), ('4', '5', '6'), ('4', '11', '19'),
         ('6', '14', '21'), ('7', '8', '9'), ('7', '12', '16'), ('9', '13', '18'), ('13', '14', '15'),
         ('10', '11', '12'), ('16', '17', '18'), ('17', '20', '23'), ('19', '20', '21'), ('22', '23', '24')]

# same for double mills
double_mills = [('1', '2', '3', '10', '22'), ('1', '2', '3', '15', '24'), ('1', '10', '22', '23', '24'),
                ('2', '5', '8', '4', '6'), ('3', '15', '24', '23', '22'), ('4', '5', '6', '11', '19'),
                ('4', '5', '6', '14', '21'), ('4', '11', '19', '20', '21'), ('4', '11', '19', '10', '12'),
                ('6', '14', '21', '20', '19'), ('6', '14', '21', '13', '15'), ('19', '20', '21', '17', '23'),
                ('7', '8', '9', '12', '16'), ('7', '8', '9', '13', '18'), ('7', '12', '16', '17', '18'),
                ('9', '13', '18', '17', '16'), ('2', '5', '7', '8', '9'), ('10', '11', '12', '7', '16'),
                ('23', '20', '17', '16', '18'), ('15', '14', '13', '9', '18'), ('1', '2', '3', '5', '8'),
                ('1', '10', '22', '11', '12'), ('22', '23', '24', '20', '17'), ('3', '15', '24', '14', '13')]

# for each place possible blocked places
# blocked = {'1': ('2', '10'), '2': ('1', '3', '5'), '3': ('2', '15'), '4': ('5', '11'), '5': ('2', '4', '6', '8'),
#            '6': ('5', '14'), '7': ('8', '12'), '8': ('5', '7', '9'), '9': ('8', '13'), '10': ('1', '11', '22'),
#            '11': ('4', '10', '12', '19'), '12': ('7', '11', '16'), '13': ('9', '14', '18'),
#            '14': ('6', '13', '15', '21'), '15': ('3', '14', '24'), '16': ('12', '17'), '17': ('16', '18', '20'),
#            '18': ('13', '17'), '19': ('11', '20'), '20': ('17', '19', '21', '23'), '21': ('14', '20'),
#            '22': ('10', '23'), '23': ('20', '22', '24'), '24': ('15', '23')}

# need one to complete a morris on two places in the same moment
need_two = [('3', '22', '1', '2', '10'), ('3', '22', '15', '23', '24'), ('1', '24', '2', '3', '15'),
            ('1', '24', '10', '22', '23'), ('6', '19', '4', '5', '11'), ('6', '19', '14', '20', '21'),
            ('4', '21', '11', '19', '20'), ('4', '21', '5', '6', '14'), ('7', '18', '12', '16', '17'),
            ('7', '18', '8', '9', '13'), ('9', '16', '7', '8', '12'), ('9', '16', '13', '17', '18'),
            ('12', '19', '4', '10', '11'), ('10', '19', '4', '11', '12'), ('4', '10', '11', '12', '19'),
            ('4', '12', '10', '11', '19'), ('17', '19', '20', '21', '23'), ('17', '21', '19', '20', '23'),
            ('19', '23', '17', '20', '21'), ('21', '23', '17', '19', '20'), ('6', '13', '14', '15', '21'),
            ('6', '15', '13', '14', '21'), ('13', '21', '6', '14', '15'), ('15', '21', '6', '13', '14'),
            ('2', '4', '5', '6', '8'), ('2', '6', '4', '5', '8'), ('4', '8', '2', '5', '6'),
            ('6', '8', '2', '4', '5'), ('2', '7', '5', '8', '9'), ('2', '9', '5', '7', '8'),
            ('10', '16', '7', '11', '12'), ('10', '7', '11', '12', '16'), ('23', '16', '17', '18', '20'),
            ('23', '18', '16', '17', '20'), ('15', '9', '13', '14', '18'), ('15', '18', '9', '13', '14'),
            ('8', '1', '2', '3', '5'), ('8', '3', '1', '2', '5'), ('12', '1', '10', '11', '22'),
            ('12', '22', '1', '10', '11'), ('17', '22', '20', '23', '24'), ('17', '24', '20', '22', '23'),
            ('13', '3', '14', '15', '24'), ('13', '24', '3', '14', '15')]

# B - human, W - computer

# Morris made in last move
def is_morris(state, pl):

    for mill in mills:
        if state._board[mill[0]] == state._board[mill[1]] == state._board[mill[2]] == pl:
            return True

    return False


def closed_morris(state): # 1.

    if morris_last(state, 'W'):
        return 1
    elif morris_last(state, 'B'):
        return -1
    else:
        return 0


# Difference between the number of yours and yours opponent’s pieces
def number_of_pieces(state, pl): # 4.

    count = 0
    for i in state._board:
        if state._board[i] == pl:
            count += 1

    return count


def number_of_pieces_diff(state):

    diff = number_of_pieces(state, 'W') - number_of_pieces(state, 'B')
    return diff


# Difference between number of yours and yours opponent’s double morrises
def heuristic_double_morris(state, pl): # 7.

    count = 0
    for dmill in double_mills:
        if state._board[dmill[0]] == state._board[dmill[1]] == state._board[dmill[2]] == state._board[dmill[3]] == \
                state._board[dmill[4]] == pl:
            count += 1

    return count


def heuristic_double_morris_diff(state):

    return heuristic_double_morris(state, 'W') - heuristic_double_morris(state, 'B')


# Difference between the number of yours and yours opponent’s morrises
def number_of_morrises(state, pl): # 2.

    count = 0
    for mill in mills:
        if state._board[mill[0]] == state._board[mill[1]] == state._board[mill[2]] == pl:
            count += 1

    return count


def number_of_morrises_diff(state):

    return number_of_morrises(state, 'W') - number_of_morrises(state, 'B')


#  Difference between the number of yours and yours opponent’s 2 piece configurations
def number_of_two_conf(state, pl): # 5.

    count = 0
    for mill in mills:
        if state._board[mill[0]] == state._board[mill[1]] == pl and state._board[mill[2]] not in "BW":
            count += 1
        elif state._board[mill[0]] == state._board[mill[2]] == pl and state._board[mill[1]] not in "BW":
            count += 1
        elif state._board[mill[1]] == state._board[mill[2]] == pl and state._board[mill[0]] not in "BW":
            count += 1
        else:
            pass

    return count


def number_of_two_conf_diff(state):

    return number_of_two_conf(state, "W") - number_of_two_conf(state, "B")


# Difference between the number of yours and yours opponent’s 3 piece configurations
def number_of_three_conf(state, pl): # 6.

    count = 0

    for three in need_two:
        if state._board[three[2]] == state._board[three[3]] == state._board[three[4]] == pl and state._board[three[0]] \
                not in 'BW' and state._board[three[1]] not in 'BW':
            count += 1

    return count


def number_of_three_conf_diff(state):

    return number_of_three_conf(state, "W") - number_of_three_conf(state, "B")


# Difference between the number of yours opponent’s and yours blocked pieces
def blocked_pieces(state, pl): # 3.

    count = 0
    if pl == "B":
        for i in blocked:
            temp = 0
            if state._board[i] == 'B':
                for j in blocked[i]:
                    if state._board[j] != 'W':
                        temp += 1
                if not temp:
                    count += 1
    else:
        for i in blocked:
            temp1 = 0
            if state._board[i] == 'W':
                for j in blocked[i]:
                    if j != 'B':
                        temp1 += 1
                if not temp1:
                    count += 1

    return count

#aj da probam
def blocked_pieces_diff(state):

    return blocked_pieces(state, 'B') - blocked_pieces(state, 'W')


def all_closed(state, pl):

    if pl == "B":
        for i in blocked:
            if state._board[i] == 'B':
                for j in blocked[i]:
                    if state._board[j] != 'W':
                        return False
        return True
    else:
        for i in blocked:
            if state._board[i] == 'W':
                for j in blocked[i]:
                    if state._board[j] != 'B':
                        return False
        return True


# we know that for a pl to win the number of opponent's pieces has to be lower than 3 or that all opponent's pieces have
# to be closed
def winning_configuration(state): # 8.

    if all_closed(state, 'B') or number_of_pieces(state, 'B'):
        return 1
    elif all_closed(state, 'W') or number_of_pieces(state, 'W'):
        return -1
    else:
        return 0


def result(state, phase):
# 18 to 38
# 14 to 38
    value = 0
    if phase == '1':
        value = 50 * closed_morris(state) + 70 * number_of_morrises_diff(state) + blocked_pieces_diff(state) + \
                9 * number_of_pieces_diff(state) + 10 * number_of_two_conf_diff(state) + \
                7 * number_of_three_conf_diff(state)

    else:
        value = 38 * closed_morris(state) + 43 * number_of_morrises_diff(state) + 10 * blocked_pieces_diff(state) + \
                11 * number_of_pieces_diff(state) + 8 * heuristic_double_morris_diff(state) + \
                1086 * winning_configuration(state)

    # print(value, state._what_is_played)

    return value


def pos_of_morris(state, pl):

    pos = []
    if state == None:
        return []
    for mill in mills:
        if state._board[mill[0]] == state._board[mill[1]] == state._board[mill[2]] == pl:
            pos.append(mill)

    return pos


def morris_last(state, pl):

    a = pos_of_morris(state._parent, pl)
    b = pos_of_morris(state, pl)

    if b:
        for i in b:
            if i not in a:
                return True
    return False


# 18 * closed_morris(state) + 26 * number_of_morrises_diff(state) + blocked_pieces_diff(state) + \
#                 9 * number_of_pieces_diff(state) + 10 * number_of_two_conf_diff(state) + \
#                 7 * number_of_three_conf_diff(state)

# Evaluation function for Phase 1 = 18 * (1) + 26 * (2) + 1 * (3) + 9 * (4) + 10 * (5) + 7 * (6)
#
# Evaluation function for Phase 2 = 14 * (1) + 43 * (2) + 10 * (3) + 11 * (4) + 8 * (7) + 1086 * (8)
# a = state.State()
# print(a._board)
# a.set_value('17', "B")
# a.set_value('20', "B")
# a.set_value('23', "B")
# print(a._board)
# print(is_mill(a))
