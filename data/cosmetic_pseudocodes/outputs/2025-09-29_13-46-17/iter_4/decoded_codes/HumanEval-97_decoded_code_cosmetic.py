from typing import Callable

def multiply(integer_a: int, integer_b: int) -> int:
    def recursive_helper(num1_alt: int, num2_alt: int, accumulator_init: int) -> int:
        if num1_alt != 0:
            return recursive_helper(num1_alt - 1, num2_alt, accumulator_init + num2_alt)
        else:
            return accumulator_init

    def get_mod_abs(val_recur: int) -> int:
        return (-val_recur if val_recur < 0 else val_recur) % 10

    mod_val1 = get_mod_abs(integer_a)
    mod_val2 = get_mod_abs(integer_b)

    return recursive_helper(mod_val1, mod_val2, 0)