from functools import cache

@cache
def fibfib(num: int) -> int:
    if num == 0 or num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibfib(num - 1) + fibfib(num - 2) + fibfib(num - 3)