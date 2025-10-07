from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    if integer_k <= 0:
        return 0
    sliced = array_of_integers[:integer_k]
    return sum(e for e in sliced if len(str(e)) <= 2)