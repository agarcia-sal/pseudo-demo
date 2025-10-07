from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def inner_loop(counter: int, accumulator: int) -> int:
        if counter >= integer_n:
            return accumulator
        else:
            return inner_loop(counter + 1, (accumulator * 2) % integer_p)
    return inner_loop(0, 1)