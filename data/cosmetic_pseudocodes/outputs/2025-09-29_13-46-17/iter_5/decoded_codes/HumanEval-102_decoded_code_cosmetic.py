from typing import Callable

def choose_num(x: int, y: int) -> int:
    a_B: int = 0
    q_k: int = 0

    def check_rec(c_r: int, v_t: int) -> int:
        if v_t % 2 == 0:
            return v_t
        if c_r == v_t:
            return -1
        return v_t - 1

    if not (x <= y):
        a_B = -1
        return a_B
    q_k = check_rec(x, y)
    return q_k