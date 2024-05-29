# Human moves in the game

import print_table as p
import state as st
import situations as s
from copy import deepcopy
import main
placed_fig = 0
placed_fig1 = 0


def phase_1(state):

    global placed_fig
    not_used = []
    last = deepcopy(state._board)
    for i in state._board:
        if state._board[i] not in "BW":
            not_used.append(i)

    p.table()
    print('=' * 40)
    print("Possible moves for player:")
    print('=' * 40)
    for i in not_used:
        print(f"Possible move: B to {p.positions[i]} ")
    print('=' * 40)
    while True:

        in1 = input("Input number on which you want to place your figure. ")
        if in1 not in not_used:
            if in1 in state._board:
                print("This place is already used. ")
            else:
                print("Unvalid input. ")
            continue
        break

    p.positions[in1] = 'B'
    placed_fig += 1
    p.table()
    state._board = last
    new = st.State(p.positions, None, state, True, (p.positions[in1], 'B'))
    if s.morris_last(new, 'B'):
        phase_mill(new)
    # control_play(new)
    main.play_game(new)


def phase_2(state):

    # global placed_fig
    not_used = []
    my = []
    last = deepcopy(state._board)
    for i in state._board:
        if state._board[i] ==  "B":
            my.append(i)
        if state._board[i] not in "BW":
            not_used.append(i)

    possible_move = []
    for i in my:
        for j in s.blocked[i]:
            if state._board[j] not in "BW":
                possible_move.append((i, j))

    print('=' *40)
    print("Possible moves for player:")
    print('=' * 40)
    for i in possible_move:
        print(f"Possible move: {s.coordinates1[i[0]]} to {s.coordinates1[i[1]]}")
    print('=' * 40)

    while True:

        inpH = input("Input position horizontal from which you want to move(a-g): ")
        if inpH not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            print("This position does not exist, try again. ")
            continue
        inpV = input("Input position vertical from which you want to move(1-7): ")
        if inpV not in ['1', '2', '3', '4', '5', '6', '7']:
            print("This position does not exist, try again. ")
            continue
        print('=' * 40)
        inpH1 = input("Input position horizontal on which you want to move(a-g): ")
        if inpH1 not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            print("This position does not exist, try again. ")
            continue
        inpV1 = input("Input position vertical on which you want to move(1-7): ")
        if inpV1 not in ['1', '2', '3', '4', '5', '6', '7']:
            print("This position does not exist, try again. ")
            continue
        print('=' * 40)
        tup = (inpV, inpH)
        tup1 = (inpV1, inpH1)
        temp = 0
        for i in possible_move:
            if s.coordinates[tup] == i[0] and s.coordinates[tup1] == i[1]:
                p.positions[s.coordinates[tup]] = s.coordinates[tup]
                p.positions[s.coordinates[tup1]] = 'B'
                temp += 1
                break
        if temp:
            break
        else:
            print("Cannot move your figure to that place")

    p.table()
    state._board = last
    new = st.State(p.positions, None, state, True, (p.positions[s.coordinates[tup1]],  'B'))
    if s.morris_last(new, 'B'):
        phase_mill(new)
    # control_play(new)
    main.play_game(new)


def phase_mill(state):

    possible = []
    last = deepcopy(state._board)
    for i in state._board:
        if state._board[i] == 'W':
            possible.append(i)

    # This part of code disables us to remove B if he has a morris too.
    op_morr = s.pos_of_morris(state, 'W')
    if op_morr:
        possible.remove(op_morr[0])
        possible.remove(op_morr[1])
        possible.remove(op_morr[2])


    print("You made a morris!")
    print("Let's remove one opponent's figure. ")

    print('=' * 40)
    print("Possible moves for player:")
    print('=' * 40)
    for i in possible:
        print(f"Possible move: remove W from {s.coordinates1[i]}")
    print('=' * 40)

    while True:

        inpH = input("Input position horizontal (a-g): ")
        if inpH not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            print("This position does not exist, try again. ")
            continue
        inpV = input("Input position vertical (1-7): ")
        if inpV not in ['1', '2', '3', '4', '5', '6', '7']:
            print("This position does not exist, try again. ")
            continue
        tup = (inpV, inpH)
        if s.coordinates[tup] in possible:
            p.positions[s.coordinates[tup]] = s.coordinates[tup]
            break
        else:
            print("Cannot remove figure on that position. ")

    p.table()
    state._board = last
    new = st.State(p.positions, None, state, True, (p.positions[s.coordinates[tup]],  s.coordinates[tup]))
    # control_play(new)
    main.play_game(new)



def control_play(state):

    # if s.morris_last(state, 'B'):
    #     phase_mill(state)
    # if not state._maxedpl:
    #     if placed_fig == 9:
    #         print("Phase 2")
    #         return
    #     else:
    #         phase_1(state)
    #
    # else:
    #     if placed_fig1 == 9:
    #         print("Phase 2")
    #         return
    #     phase_1pl2(state)
    #
    # while True:
    #     if placed_fig == 9:
    #         phase_2(state)
    #         break
    #     phase_1(state)
    if placed_fig < 9:
        if s.morris_last(state, 'B'):
            phase_mill(state)
            return
        phase_1(state)
        return
    else:
        state.end()
        if s.morris_last(state, 'B'):
            phase_mill(state)
            return
        phase_2(state)
        return

# phase_1(state.s)
# phase_1(state.s)
# phase_1(state.s)
# if s.is_morris(state.s, 'B'):
#     phase_mill(state.s)
# b = st.State(p.positions, [], None, False, None)
# control_play(b)





