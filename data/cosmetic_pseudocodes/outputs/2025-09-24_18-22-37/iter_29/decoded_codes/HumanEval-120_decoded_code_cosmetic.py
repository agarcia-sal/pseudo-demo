from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    result_sequence: List[int] = []
    if positive_integer_k != 0:
        sorted_array = sorted(array_of_integers)
        slice_start_index = len(sorted_array) - positive_integer_k
        result_sequence = sorted_array[slice_start_index:]
        return result_sequence
    return result_sequence