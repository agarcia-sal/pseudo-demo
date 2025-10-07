from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def helper(accumulator: int, counter: int) -> int:
        if counter >= integer_n:
            return accumulator
        else:
            return helper((accumulator << 1) % integer_p, counter + 1)
    return helper(1, 0)