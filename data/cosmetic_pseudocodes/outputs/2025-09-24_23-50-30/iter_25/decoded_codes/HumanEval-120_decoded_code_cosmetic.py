from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    array_of_integers.sort()
    total_len = len(array_of_integers)
    start_index = total_len - positive_integer_k
    return array_of_integers[start_index:total_len]