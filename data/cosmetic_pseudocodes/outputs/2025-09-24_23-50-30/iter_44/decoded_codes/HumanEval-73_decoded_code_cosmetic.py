from typing import Sequence


def smallest_change(collection_of_numbers: Sequence[int]) -> int:
    result_counter = 0
    midpoint = len(collection_of_numbers) // 2

    for i in range(midpoint):
        if collection_of_numbers[i] != collection_of_numbers[len(collection_of_numbers) - (i + 1)]:
            result_counter += 1

    return result_counter