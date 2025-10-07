from typing import Callable

def fib(numValue: int) -> int:
    def helper(counter: int) -> int:
        if counter == 0:
            return 0
        elif counter == 1:
            return 1
        else:
            return helper(counter - 1) + helper(counter - 2)
    return helper(numValue)