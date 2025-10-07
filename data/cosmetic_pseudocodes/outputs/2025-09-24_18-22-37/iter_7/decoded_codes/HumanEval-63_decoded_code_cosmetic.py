from typing import Literal

def fibfib(number_x: int) -> int:
    if number_x == 0:
        return 0
    elif number_x == 1:
        return 0
    elif number_x == 2:
        return 1
    else:
        return fibfib(number_x - 1) + fibfib(number_x - 2) + fibfib(number_x - 3)