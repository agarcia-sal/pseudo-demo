from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    if positive_integer_k < 0:
        # If k is negative, return empty list since semantics unclear; alternatively, could raise error
        return []
    sorted_arr = sorted(array_of_integers)
    return sorted_arr[-positive_integer_k:]