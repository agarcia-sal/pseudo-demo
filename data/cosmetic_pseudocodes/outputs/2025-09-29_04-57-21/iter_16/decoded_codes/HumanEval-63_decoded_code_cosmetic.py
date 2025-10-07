from typing import Union

def fibfib(integer_n: int) -> int:
    if integer_n == 0:
        return 0
    if integer_n == 1:
        return 0
    if integer_n == 2:
        return 1

    delta1 = integer_n - 1
    delta2 = integer_n - 2
    delta3 = integer_n - 3

    return fibfib(delta1) + fibfib(delta2) + fibfib(delta3)