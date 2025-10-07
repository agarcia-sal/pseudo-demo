from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def helper(counter: int, acc: int) -> int:
        if counter == integer_n:
            return acc
        else:
            return helper(counter + 1, (acc * 2) % integer_p)
    return helper(0, 1)