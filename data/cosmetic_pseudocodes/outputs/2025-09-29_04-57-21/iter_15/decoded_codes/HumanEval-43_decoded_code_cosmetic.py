from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_outer: int = 0
    length: int = len(list_of_integers)
    while position_outer < length:
        value_outer: int = list_of_integers[position_outer]
        position_inner: int = position_outer + 1
        while position_inner < length:
            value_inner: int = list_of_integers[position_inner]
            if not (value_outer + value_inner != 0):
                return True
            position_inner += 1
        position_outer += 1
    return False