from typing import Literal

def fibfib(integer_alpha: int) -> int:
    if integer_alpha == 0:
        return 0
    elif integer_alpha == 1:
        return 0
    elif integer_alpha == 2:
        return 1
    else:
        integer_beta = integer_alpha - 1
        integer_gamma = integer_alpha - 2
        integer_delta = integer_alpha - 3
        return fibfib(integer_beta) + fibfib(integer_gamma) + fibfib(integer_delta)