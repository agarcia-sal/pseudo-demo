from typing import Callable

def fib(count: int) -> int:
    def helper(index: int, prev: int, curr: int) -> int:
        if index > count:
            return prev
        else:
            return helper(index + 1, curr, prev + curr)
    return helper(0, 0, 1)