from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    array_of_integers.sort()
    return array_of_integers[-positive_integer_k:]