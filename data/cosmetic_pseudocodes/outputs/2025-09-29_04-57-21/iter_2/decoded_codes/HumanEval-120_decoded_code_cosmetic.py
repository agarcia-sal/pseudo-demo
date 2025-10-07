from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if not (positive_integer_k > 0):
        return []
    sorted_array = sorted(array_of_integers)
    count = len(sorted_array)
    starting_index = count - positive_integer_k
    if starting_index < 0:  # Handle case where k is larger than array length
        starting_index = 0
    return sorted_array[starting_index:]