from typing import List


def f(integer_n: int) -> List[int]:
    output_sequence: List[int] = []

    def helper_factorial(x: int, accumulator: int) -> int:
        if x == 0:
            return accumulator
        return helper_factorial(x - 1, accumulator * x)

    def helper_sum(limit: int) -> int:
        return (limit * (limit + 1)) // 2

    for index_counter in range(1, integer_n + 1):
        if (index_counter & 1) == 0:
            computed_value = helper_factorial(index_counter, 1)
        else:
            computed_value = helper_sum(index_counter)
        output_sequence.append(computed_value)

    return output_sequence