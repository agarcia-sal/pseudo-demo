from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    start_idx = len(sorted_array) - positive_integer_k
    if start_idx < 0:
        start_idx = 0
    return [sorted_array[i] for i in range(start_idx, len(sorted_array))]