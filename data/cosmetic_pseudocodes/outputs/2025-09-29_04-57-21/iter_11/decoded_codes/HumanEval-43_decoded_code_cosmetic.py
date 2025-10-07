from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    pos_outer: int = 0
    length: int = len(list_of_integers)
    while pos_outer < length:
        current_val: int = list_of_integers[pos_outer]
        pos_inner: int = pos_outer + 1
        while pos_inner < length:
            if list_of_integers[pos_inner] + current_val == 0:
                return True
            pos_inner += 1
        pos_outer += 1
    return False