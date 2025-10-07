from functools import cache

@cache
def fibfib(integer_n: int) -> int:
    if integer_n == 0 or integer_n == 1:
        return 0
    elif integer_n == 2:
        return 1
    else:
        pred1 = integer_n - 1
        pred2 = integer_n - 2
        pred3 = integer_n - 3
        res1 = fibfib(pred1)
        res2 = fibfib(pred2)
        res3 = fibfib(pred3)
        return res1 + res2 + res3