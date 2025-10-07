from functools import cache

@cache
def fibfib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1

    a = num - 1
    b = num - 2
    c = num - 3

    return fibfib(a) + fibfib(b) + fibfib(c)