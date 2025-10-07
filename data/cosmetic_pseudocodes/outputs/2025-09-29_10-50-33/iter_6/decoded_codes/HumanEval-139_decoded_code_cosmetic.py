from typing import Callable

def special_factorial(integer_n: int) -> int:
    def recursive_product(current_index: int, accum_factorial: int, accum_special: int) -> int:
        if current_index > integer_n:
            return accum_special
        updated_factorial = accum_factorial * current_index
        updated_special = accum_special * updated_factorial
        return recursive_product(current_index + 1, updated_factorial, updated_special)
    return recursive_product(1, 1, 1)