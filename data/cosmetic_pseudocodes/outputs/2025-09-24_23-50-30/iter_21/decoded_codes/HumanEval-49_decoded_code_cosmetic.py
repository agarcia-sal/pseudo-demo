from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def helper(counter: int, accumulator: int) -> int:
        if counter == integer_n:
            return accumulator
        else:
            return helper(counter + 1, (accumulator + accumulator) % integer_p)
    return helper(0, 1)