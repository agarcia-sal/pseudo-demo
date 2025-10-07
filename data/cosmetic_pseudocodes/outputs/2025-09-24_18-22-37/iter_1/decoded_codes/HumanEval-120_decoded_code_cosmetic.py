from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    length = len(sorted_array)
    return sorted_array[length - positive_integer_k : length]