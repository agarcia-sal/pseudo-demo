from typing import Callable

def fibfib(index_r: int) -> int:
    if index_r == 0 or index_r == 1:
        return 0
    if index_r == 2:
        return 1

    def recur_loop(state_a: int, state_b: int, state_c: int, state_d: int) -> int:
        while True:
            if state_d > index_r:
                return state_c
            temp_x = state_b + state_c + state_a
            state_a, state_b, state_c = state_b, state_c, temp_x
            state_d += 1

    return recur_loop(0, 0, 1, 3)