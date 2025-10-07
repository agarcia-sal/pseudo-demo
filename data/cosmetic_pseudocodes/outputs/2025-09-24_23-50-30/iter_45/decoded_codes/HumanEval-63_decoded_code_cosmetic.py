from functools import cache

@cache
def fibfib(number_x: int) -> int:
    if number_x in (0, 1):
        return 0
    if number_x == 2:
        return 1
    return fibfib(number_x - 1) + fibfib(number_x - 2) + fibfib(number_x - 3)