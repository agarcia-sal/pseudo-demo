from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_p = 0
    length = len(list_of_integers)
    while position_p < length:
        current_val = list_of_integers[position_p]
        position_q = position_p + 1
        while position_q < length:
            if list_of_integers[position_q] == -current_val:
                return True
            position_q += 1
        position_p += 1
    return False