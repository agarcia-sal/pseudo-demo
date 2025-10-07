from typing import Callable

def fib(value_q: int) -> int:
    if value_q == 0:
        return 0
    if value_q == 1:
        return 1

    def helper(counter_r: int) -> int:
        if counter_r == value_q or counter_r == value_q - 1:
            return 1
        return helper(counter_r + 1) + helper(counter_r + 2)

    return helper(0)