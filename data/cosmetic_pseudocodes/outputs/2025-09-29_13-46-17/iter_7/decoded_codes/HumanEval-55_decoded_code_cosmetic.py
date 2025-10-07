from typing import Callable

def fib(xQ9: int) -> int:
    if xQ9 == 0:
        return 0
    if xQ9 == 1:
        return 1

    def U7f(A1B: int, K9m: int) -> int:
        while True:
            if A1B == K9m:
                return A1B
            A1B += 1

    return U7f(fib(xQ9 - 1), fib(xQ9 - 2))