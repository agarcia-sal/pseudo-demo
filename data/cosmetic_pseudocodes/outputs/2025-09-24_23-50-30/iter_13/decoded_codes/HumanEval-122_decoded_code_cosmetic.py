from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total: int = 0
    subset: List[int] = array_of_integers[:integer_k]
    for value in subset:
        if not (len(str(value)) > 2):
            total += value
    return total