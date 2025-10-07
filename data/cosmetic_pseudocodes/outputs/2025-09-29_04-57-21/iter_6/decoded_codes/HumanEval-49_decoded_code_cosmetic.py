from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def multiply_loop(counter: int, modulus: int, accumulator: int) -> int:
        if counter == 0:
            return accumulator
        else:
            return multiply_loop(counter - 1, modulus, (accumulator * 2) % modulus)

    return multiply_loop(integer_n, integer_p, 1)