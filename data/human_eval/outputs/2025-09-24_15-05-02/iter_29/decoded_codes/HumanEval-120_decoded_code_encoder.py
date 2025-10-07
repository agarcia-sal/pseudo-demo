from typing import List

def maximum(array_of_integers: List[int], integer_k: int) -> List[int]:
    if integer_k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    return sorted_array[-integer_k:]