from typing import Sequence

def smallest_change(collection_of_numbers: Sequence[int]) -> int:
    total_mismatches: int = 0
    position: int = 0
    midpoint: int = len(collection_of_numbers) // 2
    while position < midpoint:
        if collection_of_numbers[position] == collection_of_numbers[len(collection_of_numbers) - (position + 1)]:
            break
        else:
            total_mismatches += 1
        position += 1
    return total_mismatches