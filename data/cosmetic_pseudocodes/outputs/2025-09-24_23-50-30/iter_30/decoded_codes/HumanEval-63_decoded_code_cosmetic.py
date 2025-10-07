from functools import cache

@cache
def fibfib(integer_x: int) -> int:
    if integer_x == 0 or integer_x == 1:
        return 0
    if integer_x == 2:
        return 1
    return fibfib(integer_x - 1) + fibfib(integer_x - 2) + fibfib(integer_x - 3)