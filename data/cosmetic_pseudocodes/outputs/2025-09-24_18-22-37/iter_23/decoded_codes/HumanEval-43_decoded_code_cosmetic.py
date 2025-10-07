from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_m: int = 0
    length: int = len(list_of_integers)
    while position_m < length:
        value_p: int = list_of_integers[position_m]
        position_q: int = position_m + 1
        while position_q <= length - 1:
            value_r: int = list_of_integers[position_q]
            sum_temp: int = value_p + value_r
            if sum_temp == 0:
                return True
            position_q += 1
        position_m += 1
    return False