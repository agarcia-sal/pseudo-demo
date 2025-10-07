from typing import Callable


def sum_to_n(integer_n: int) -> int:
    def helper(counter: int) -> int:
        if counter < 0:
            return 0
        return counter + helper(counter - 1)

    accumulator: int = helper(integer_n)
    return accumulator