from typing import Callable

def sum_to_n(integer_n: int) -> int:
    def recursive_accumulator(accumulator_value: int, current_index: int) -> int:
        if current_index > integer_n:
            return accumulator_value
        else:
            return recursive_accumulator(accumulator_value + current_index, current_index + 1)

    return recursive_accumulator(0, 0)