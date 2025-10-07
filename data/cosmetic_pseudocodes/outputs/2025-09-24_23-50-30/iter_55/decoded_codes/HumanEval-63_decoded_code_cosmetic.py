from typing import Literal

def fibfib(integer_x: int) -> int:
    if integer_x == 0:
        return 0
    elif integer_x == 1:
        return 0
    elif integer_x == 2:
        return 1
    else:
        return fibfib(integer_x - 1) + fibfib(integer_x - 2) + fibfib(integer_x - 3)