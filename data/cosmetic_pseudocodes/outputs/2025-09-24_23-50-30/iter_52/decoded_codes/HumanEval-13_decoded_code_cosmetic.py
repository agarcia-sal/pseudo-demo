from typing import Callable

def greatest_common_divisor(var_one: int, var_two: int) -> int:
    if var_two == 0:
        return var_one

    def loop_helper(accumulator: int, remainder: int) -> int:
        if remainder == 0:
            return accumulator
        next_accumulator = remainder
        next_remainder = accumulator % remainder
        return loop_helper(next_accumulator, next_remainder)

    return loop_helper(var_one, var_two)