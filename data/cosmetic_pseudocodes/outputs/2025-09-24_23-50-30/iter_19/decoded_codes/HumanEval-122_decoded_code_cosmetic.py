from typing import Sequence


def add_elements(idx_values: Sequence[int], limit: int) -> int:
    total_accumulator = 0
    index_counter = 0
    while index_counter < limit:
        if len(str(idx_values[index_counter])) <= 2:
            total_accumulator += idx_values[index_counter]
        index_counter += 1
    return total_accumulator