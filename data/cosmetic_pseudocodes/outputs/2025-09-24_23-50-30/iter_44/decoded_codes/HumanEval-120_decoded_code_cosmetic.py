from typing import List

def maximum(array_of_integers: List[int], positive_integer_m: int) -> List[int]:
    if positive_integer_m == 0:
        return []
    sorted_array = sorted(array_of_integers)
    start_index = len(sorted_array) - positive_integer_m
    # Slicing handles cases where m > length(array_of_integers) gracefully
    return sorted_array[max(start_index, 0):]