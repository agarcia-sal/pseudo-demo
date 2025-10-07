from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    acc_multiplicand: int = 2
    max_iterations: int = integer_n - 1
    accumulator: int = 1

    def helper(loop_counter: int) -> int:
        nonlocal accumulator
        if loop_counter > max_iterations:
            return accumulator
        accumulator = (accumulator * acc_multiplicand) - (integer_p * ((accumulator * acc_multiplicand) // integer_p))
        return helper(loop_counter + 1)

    return helper(0)