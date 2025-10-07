from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    counter_m: int = 0
    length: int = len(list_of_integers)
    while counter_m < length:
        variable_p: int = list_of_integers[counter_m]
        counter_q: int = counter_m + 1
        while counter_q < length:
            sum_tmp: int = variable_p + list_of_integers[counter_q]
            if sum_tmp == 0:
                return True
            counter_q += 1
        counter_m += 1
    return False