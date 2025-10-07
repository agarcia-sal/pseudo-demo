from typing import Callable


def sum_to_n(num_x: int) -> int:
    def recursive_sum(current_i: int, accumulator_j: int) -> int:
        if current_i > num_x:
            return accumulator_j
        else:
            return recursive_sum(current_i + 1, accumulator_j + current_i)
    return recursive_sum(0, 0)