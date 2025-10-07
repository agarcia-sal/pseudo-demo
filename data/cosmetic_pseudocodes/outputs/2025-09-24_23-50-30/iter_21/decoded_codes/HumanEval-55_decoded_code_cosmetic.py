from typing import Union

def fib(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a: int = 0
        b: int = 1
        c: int = 0
        idx: int = 2

        while idx <= num:
            c = a + b
            a = b
            b = c
            idx += 1

        return c