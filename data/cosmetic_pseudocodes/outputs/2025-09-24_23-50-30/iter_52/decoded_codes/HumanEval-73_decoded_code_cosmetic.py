from typing import Sequence

def smallest_change(collection_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    limit: int = (len(collection_of_numbers) // 2) - 1

    def helper(current_index: int) -> int:
        nonlocal accumulator
        if current_index > limit:
            return accumulator
        if collection_of_numbers[current_index] != collection_of_numbers[len(collection_of_numbers) - current_index - 1]:
            accumulator += 1
        return helper(current_index + 1)

    return helper(0)