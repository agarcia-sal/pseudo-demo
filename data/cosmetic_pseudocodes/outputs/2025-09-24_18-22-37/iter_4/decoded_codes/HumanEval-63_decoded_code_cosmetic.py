from functools import cache

@cache
def fibfib(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a = fibfib(num - 1)
        b = fibfib(num - 2)
        c = fibfib(num - 3)
        return a + b + c