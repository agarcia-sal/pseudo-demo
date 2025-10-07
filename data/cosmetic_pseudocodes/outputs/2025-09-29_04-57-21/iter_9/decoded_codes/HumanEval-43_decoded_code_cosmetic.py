from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_pos: int = 0
    length: int = len(list_of_integers)
    while outer_pos < length:
        outer_val: int = list_of_integers[outer_pos]
        inner_pos: int = outer_pos + 1
        while inner_pos < length:
            inner_val: int = list_of_integers[inner_pos]
            if not (outer_val + inner_val) != 0:
                return True
            inner_pos += 1
        outer_pos += 1
    return False