from copy import deepcopy
import state as st
import math
import situations as sit
import human_side as h
import print_table as p
import time
import main
import time
a = math.inf
b = - math.inf
comp_placed = 0


def minimax(state, alpha, beta, depth, maxingpl):

    if depth == 0:
        return sit.result(state, control_phase(state, pl(maxingpl))), state._what_is_played

    if maxingpl:
        max_eval = - math.inf
        best = None
        call_phase(state, control_phase(state, pl(maxingpl)))
        for each in state._next:
            move = each._what_is_played
            evaluate, mov = minimax(each, alpha, beta, depth - 1, False)
            max_eval = max(max_eval, evaluate)
            alpha = max(alpha, evaluate)
            if beta <= alpha:
                break

            if max_eval <= evaluate:
                best =  move

        return max_eval, best

    else:
        min_eval = math.inf
        best = None
        call_phase(state, control_phase(state, pl(maxingpl)))
        for each in state._next:
            move = each._what_is_played
            evaluate, mov = minimax(each, alpha, beta, depth - 1, True)
            min_eval = min(min_eval, evaluate)
            beta = min(beta, evaluate)
            if beta <= alpha:
                break

            if min_eval >= evaluate:
                best =  move

        return min_eval, best
# def minimax(state, alpha, beta, depth, maxingpl):
#
#     if depth == 0:
#         return sit.result(state, control_phase(state, pl(maxingpl)))
#
#     if maxingpl:
#         return maximum(state, alpha, beta, depth, maxingpl)
#     else:
#         return minimum(state, alpha, beta, depth, maxingpl)


# def maximum(state, alpha, beta, depth, maxingpl):
#
#     max_eval = - math.inf
#     call_phase(state, control_phase(state, pl(maxingpl)))
#     for each in state._next:
#         evaluate = minimax(each, alpha, beta, depth - 1, False)
#         max_eval = max(max_eval, evaluate)
#         alpha = max(alpha, evaluate)
#         if beta <= alpha:
#             break
#     return max_eval
#
#
# def minimum(state, alpha, beta, depth, maxingpl):
#
#     min_eval = math.inf
#     call_phase(state, control_phase(state, pl(maxingpl)))
#     for each in state._next:
#         evaluate = minimax(each, alpha, beta, depth - 1, True)
#         min_eval = min(min_eval, evaluate)
#         beta = min(beta, evaluate)
#         if beta <= alpha:
#             break
#     return min_eval


# def play_com(state):
#
#     move = ''
#     alpha = -math.inf
#     beta = math.inf
#     call_phase(state, control_phase(state, pl(True)))
#     for each in state._next:
#         # move = each._what_is_played
#         score = minimax(each, alpha, beta,3, True)
#         if score >= alpha:
#             alpha = score
#             move = each._what_is_played
#         if score <= beta:
#             beta = score
#         if alpha >= beta:
#             break
#     return move


def com_move(state, depth):

    # state.next_mill()
    # for i in state._next:
    #     print(i)
    # return
    start_time = time.time()
    global comp_placed
    phase = control_phase(state, 'W')
    last = deepcopy(state._board)

    val, move = minimax(state, -math.inf, math.inf, depth, state._maxedpl)

    if phase == '1':
        p.positions[move[0]] = move[1]
        p.table()
        print(f"Computer played {move[1]} on position {sit.coordinates1[str(move[0])]}")
        comp_placed += 1
        state._board = last
        new = st.State(p.positions, [], state, False, move)
        phase = control_phase(new, 'W')
        if phase == 'mill':
            val, move = minimax(new, -math.inf, math.inf, depth, new._maxedpl)
            p.positions[move[0]] = move[0]
            p.table()
            new._board = last
            print(f"Computer removed 'B' from position {sit.coordinates1[str(move[0])]}")
            new1 = st.State(p.positions, [], new, False, move)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            main.play_game(new1)
        else:
            new._next = []
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            main.play_game(new)

    if phase == '2':
        # p.positions[move[0]] = move[0]
        p.positions[move[0]] = 'W'
        if sit.blocked[move[0]]:
            for i in sit.blocked[move[0]]:
                if p.positions[i] == 'W':
                    p.positions[i] = i
                    break
        p.table()
        print(f"Computer played 'W' on position {sit.coordinates1[str(move[0])]}")
        state._board = last
        new = st.State(p.positions, [], state, False, move)
        phase = control_phase(new, 'W')
        if phase == 'mill':
            val, move = minimax(new, -math.inf, math.inf, depth, new._maxedpl)
            p.positions[move[0]] = move[0]
            p.table()
            new._board = last
            print(f"Computer removed 'B' from position {sit.coordinates1[str(move[0])]}")
            new1 = st.State(p.positions, [], new, False, move)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Time: ", elapsed_time)
            main.play_game(new1)
        else:
            new._next = []
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            main.play_game(new)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    main.play_game(new)


def control_phase(state, pl):

    global comp_placed
    if pl == 'W':
        if sit.morris_last(state, 'W'):
            state._maxedpl = True
            return 'mill'
        if comp_placed < 9:
            return '1'
        else:
            return '2'
    else:
        if sit.morris_last(state, 'B'):
            return 'mill'
        if comp_placed < 9:
            return '1'
        else:
            return '2'


def call_phase(state, phase):

    if phase == 'mill':
        state.next_mill()
    elif phase == '1':
        state.next_phase1()
    else:
        state.next_phase2()


def pl(maxed):

    if maxed:
        return 'W'
    else:
        return 'B'



# print(minimax(h.b, -math.inf, math.inf, 3, True))
# print(nesto)

# start_time = time.time()
#
# print(com_move(h.b))
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)
# nes = play_com(h.b)
# p.positions[nes[0]] = nes[1]
# print(play_com(p.positions))

# print(sit.result(h.b, control_phase(h.b, pl(True))))
# print(call_phase(h.b, '1'))
