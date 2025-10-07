from typing import List

def maximum(collection_of_numbers: List[float], count_positive: int) -> List[float]:
    if count_positive == 0:
        return []
    collection_of_numbers.sort()
    length_val = len(collection_of_numbers)
    start_index = length_val - count_positive
    return [collection_of_numbers[i] for i in range(start_index, length_val)]