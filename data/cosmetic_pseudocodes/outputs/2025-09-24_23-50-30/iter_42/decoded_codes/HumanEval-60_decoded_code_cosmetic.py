from typing import Callable

def sum_to_n(number_q: int) -> int:
    def tail_sum_loop(index_r: int, accumulator_s: int) -> int:
        if index_r > number_q:
            return accumulator_s
        return tail_sum_loop(index_r + 1, accumulator_s + index_r)
    return tail_sum_loop(0, 0)