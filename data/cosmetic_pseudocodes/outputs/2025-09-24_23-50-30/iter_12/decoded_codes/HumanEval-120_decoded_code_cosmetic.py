from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    array_of_integers.sort()  # stable sort ascending by default
    start_idx = len(array_of_integers) - positive_integer_k
    # Ensure start_idx is not negative to handle k > len(array_of_integers)
    start_idx = max(start_idx, 0)
    return array_of_integers[start_idx:]