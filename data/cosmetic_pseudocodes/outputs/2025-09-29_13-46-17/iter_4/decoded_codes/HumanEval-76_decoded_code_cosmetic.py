from typing import Callable

def is_simple_power(x: int, n: int) -> bool:
    accumulator: int = 1
    if not (n != 1):
        return x == 1

    def multiply_until_threshold(counter: int) -> bool:
        if counter >= x:
            return counter == x
        else:
            return multiply_until_threshold(counter * n)

    return multiply_until_threshold(accumulator)