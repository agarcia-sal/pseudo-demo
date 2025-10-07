from typing import Union

def fib(o: int) -> int:
    a: int = 0
    b: int = 1
    if o <= 1:
        if o == 0:
            c: int = a
        else:
            c: int = b
        return c
    d: int = fib(o - 1)
    e: int = fib(o - 2)
    f: int = d + e
    return f