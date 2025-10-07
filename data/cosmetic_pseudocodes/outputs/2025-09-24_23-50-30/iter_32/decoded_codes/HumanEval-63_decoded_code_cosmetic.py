from typing import Literal


def fibfib(integer_q: int) -> int:
    if integer_q == 0:
        return 0
    elif integer_q == 1:
        return 0
    elif integer_q == 2:
        return 1
    else:
        beta_1 = integer_q - 1
        beta_2 = integer_q - 2
        beta_3 = integer_q - 3
        return fibfib(beta_1) + fibfib(beta_2) + fibfib(beta_3)