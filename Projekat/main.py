import state
import human_side as hum
import computer_side as com
import print_table as p
import time

def play_game(state):

    temp = 0
    dep = 2
    while True:
        #
        if not state._maxedpl:
            hum.control_play(state)
            # state._maxedpl = True
        else:
            start_time = time.time()
            com.com_move(state, dep)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            state._maxedpl = False
            temp += 1

        if temp > 5:
            dep = 3


if __name__ == '__main__':
    print("="*30)
    print("WELCOME TO NINE MEN'S MORRIS")
    print("=" * 30)
    print("You are B and computer is W. ")
    print("=" * 30)
    play_game(state.State(p.positions, [], None, False, None))
