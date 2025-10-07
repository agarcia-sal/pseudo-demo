from typing import Callable


def modp(integer_N: int, integer_M: int) -> int:
    def helper(counter: int, acc: int) -> int:
        if counter > 0:
            return helper(counter - 1, (acc + acc) % integer_M)
        else:
            return acc

    return helper(integer_N, 1)