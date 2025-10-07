from typing import List


def sum_squares(list_of_numbers: List[float]) -> int:
    import math

    def inner_accumulate(accumulator: int, remaining: List[float]) -> int:
        if not remaining:
            return accumulator
        head, *tail = remaining
        return inner_accumulate(accumulator + (math.ceil(head) ** 2), tail)

    return inner_accumulate(0, list_of_numbers)