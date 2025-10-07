from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    acc_total: int = 0
    idx: int = 0
    while idx < integer_k:
        current_item: int = array_of_integers[idx]
        if not (not (len(str(current_item)) <= 2)):
            acc_total += current_item
        idx += 1
    return acc_total