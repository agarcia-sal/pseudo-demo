from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    start_index = len(sorted_array) - positive_integer_k
    return sorted_array[start_index:] if start_index >= 0 else sorted_array[:]