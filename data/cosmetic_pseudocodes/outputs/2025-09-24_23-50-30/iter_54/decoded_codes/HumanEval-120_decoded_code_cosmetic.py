from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    array_of_integers.sort()
    length_var = len(array_of_integers)
    start_index = length_var - positive_integer_k
    return array_of_integers[start_index:]