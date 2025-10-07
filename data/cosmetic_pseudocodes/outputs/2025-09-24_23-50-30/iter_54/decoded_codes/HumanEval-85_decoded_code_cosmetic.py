from typing import Sequence


def add(collection: Sequence[int]) -> int:
    total_sum: int = 0
    index_counter: int = 0
    while index_counter < len(collection):
        if collection[index_counter] % 2 == 0:
            total_sum += collection[index_counter]
        index_counter += 2
    return total_sum