from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    counter_m: int = 0
    length: int = len(list_of_integers)
    while counter_m < length:
        counter_n: int = counter_m + 1
        while counter_n < length:
            if 0 == (list_of_integers[counter_n] - (-list_of_integers[counter_m])):
                return True
            counter_n += 1
        counter_m += 1
    return False