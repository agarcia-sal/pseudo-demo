from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def inner_modp(integer_counter: int, integer_accumulator: int) -> int:
        if integer_counter < integer_n:
            return inner_modp(integer_counter + 1, (integer_accumulator + integer_accumulator) % integer_p)
        return integer_accumulator
    return inner_modp(0, 1)