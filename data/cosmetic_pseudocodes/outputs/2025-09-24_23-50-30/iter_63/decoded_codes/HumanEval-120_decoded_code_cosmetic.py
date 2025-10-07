from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    # sort array in ascending order
    array_of_integers.sort()
    length_of_arr = len(array_of_integers)
    start_index = length_of_arr - positive_integer_k
    # collect last k elements
    return [array_of_integers[idx] for idx in range(start_index, length_of_arr)]