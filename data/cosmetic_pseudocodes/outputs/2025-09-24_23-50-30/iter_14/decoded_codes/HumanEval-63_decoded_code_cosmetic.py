from typing import Union

def fibfib(number_x: int) -> int:
    if number_x == 0 or number_x == 1:
        return 0
    if number_x == 2:
        return 1
    return fibfib(number_x - 1) + fibfib(number_x - 2) + fibfib(number_x - 3)