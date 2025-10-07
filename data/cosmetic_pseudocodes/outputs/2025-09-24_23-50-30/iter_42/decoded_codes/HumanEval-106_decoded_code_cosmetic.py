from collections import deque
from typing import Deque

def f(integer_n: int) -> Deque[int]:
    result_accumulator: Deque[int] = deque()

    def compute_accumulation(current_index: int, accumulator: Deque[int]) -> Deque[int]:
        if current_index > integer_n:
            return accumulator

        if current_index % 2 == 0:
            factorial_result = 1
            counter = current_index
            while counter > 1:
                factorial_result *= counter
                counter -= 1
            accumulator.append(factorial_result)
        else:
            sum_result = current_index * (current_index + 1) // 2
            accumulator.append(sum_result)

        return compute_accumulation(current_index + 1, accumulator)

    final_list = compute_accumulation(1, result_accumulator)
    return final_list