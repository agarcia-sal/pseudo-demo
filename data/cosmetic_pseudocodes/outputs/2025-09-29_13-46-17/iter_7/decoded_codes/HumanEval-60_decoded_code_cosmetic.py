from typing import Callable

def sum_to_n(integer_n: int) -> int:
    def calc_y29a(alpha_n: int, zeta_acc: int) -> int:
        if alpha_n < 0:
            return zeta_acc
        else:
            return calc_y29a(alpha_n - 1, zeta_acc + alpha_n)
    return calc_y29a(integer_n, 0)