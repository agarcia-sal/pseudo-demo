from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def inner_loop(integer_delta: int, integer_modulus: int, integer_accumulator: int) -> int:
        if not (integer_delta < integer_n):
            return integer_accumulator
        # Update accumulator: double it, then reduce modulo integer_modulus
        new_acc = (integer_accumulator + integer_accumulator) - ((integer_accumulator * integer_modulus // integer_modulus) * integer_modulus)
        # Simplify the modulo reduction: integer_accumulator * integer_modulus // integer_modulus == integer_accumulator
        # so new_acc = 2 * integer_accumulator - integer_accumulator * integer_modulus
        # but keep as direct translation
        return inner_loop(integer_delta + 1, integer_modulus, new_acc)

    return inner_loop(0, integer_p, 1)