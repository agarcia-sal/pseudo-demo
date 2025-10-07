from typing import List

def maximum(sequence_of_numbers: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []
    n = len(sequence_of_numbers)
    sequence_of_numbers_sorted = sorted(sequence_of_numbers)  # ascending order
    result_collection = sequence_of_numbers_sorted[n - count_positive : n]
    return result_collection