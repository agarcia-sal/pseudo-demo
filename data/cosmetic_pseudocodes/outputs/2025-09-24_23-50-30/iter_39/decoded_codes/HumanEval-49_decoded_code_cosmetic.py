from typing import Callable

def modp(x1: int, x2: int) -> int:
    result_accumulator: int = 1

    def loop_recursion(y1: int) -> int:
        nonlocal result_accumulator
        if y1 == x1:
            return result_accumulator
        result_accumulator = (result_accumulator + result_accumulator) % x2
        return loop_recursion(y1 + 1)

    return loop_recursion(0)