from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    array_of_integers_sorted = sorted(array_of_integers)
    n = len(array_of_integers_sorted)
    return array_of_integers_sorted[max(n - positive_integer_k, 0):n]