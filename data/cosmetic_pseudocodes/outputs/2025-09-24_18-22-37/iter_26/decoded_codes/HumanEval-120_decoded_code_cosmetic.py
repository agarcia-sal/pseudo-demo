from typing import List

def maximum(numbers: List[int], count: int) -> List[int]:
    if count != 0:
        numbers_sorted = sorted(numbers)
        length_val = len(numbers_sorted)
        start_index = length_val - count
        return numbers_sorted[start_index:length_val]
    return []