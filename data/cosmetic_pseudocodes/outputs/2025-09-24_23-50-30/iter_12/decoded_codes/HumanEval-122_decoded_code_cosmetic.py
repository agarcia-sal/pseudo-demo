from typing import Sequence


def add_elements(collection_numbers: Sequence[int], limit_count: int) -> int:
    def helper(index_current: int, accumulator_sum: int) -> int:
        if index_current >= limit_count:
            return accumulator_sum
        current_value = collection_numbers[index_current]
        if len(str(current_value)) <= 2:
            new_sum = accumulator_sum + current_value
        else:
            new_sum = accumulator_sum
        return helper(index_current + 1, new_sum)

    return helper(0, 0)