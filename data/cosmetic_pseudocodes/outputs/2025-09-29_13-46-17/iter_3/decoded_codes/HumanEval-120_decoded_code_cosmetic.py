from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k <= 0:
        return []
    array_of_integers.sort()
    length_value = len(array_of_integers)
    start_index = length_value - positive_integer_k
    return array_of_integers[start_index:length_value]