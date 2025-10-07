from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k <= 0:
        return []
    sorted_values = sorted(array_of_integers)
    start_index = len(sorted_values) - positive_integer_k
    # start_index can be negative if positive_integer_k > len(sorted_values),
    # slicing handles that by starting from 0 implicitly
    result = [sorted_values[i] for i in range(start_index, len(sorted_values))]
    return result