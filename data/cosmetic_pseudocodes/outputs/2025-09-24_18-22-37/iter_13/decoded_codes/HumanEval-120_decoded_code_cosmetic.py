from typing import List

def maximum(numbers_collection: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []
    sorted_numbers = sorted(numbers_collection)
    start_index = len(sorted_numbers) - count_positive
    return sorted_numbers[start_index:]