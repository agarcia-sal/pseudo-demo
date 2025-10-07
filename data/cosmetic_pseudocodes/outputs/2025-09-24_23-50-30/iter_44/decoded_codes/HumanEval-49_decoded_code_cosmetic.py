from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def inner_loop(counter_x: int, accumulator_y: int) -> int:
        if counter_x == integer_n:
            return accumulator_y
        return inner_loop(counter_x + 1, (accumulator_y * 2) % integer_p)
    return inner_loop(0, 1)