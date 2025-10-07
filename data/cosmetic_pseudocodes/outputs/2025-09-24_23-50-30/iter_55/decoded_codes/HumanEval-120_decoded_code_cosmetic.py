from typing import List

def maximum(collection_of_numbers: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []
    sorted_sequence = sorted(collection_of_numbers)
    selection = sorted_sequence[len(sorted_sequence) - count_positive : len(sorted_sequence)]
    return selection