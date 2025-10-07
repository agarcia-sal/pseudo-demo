from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    counter_m: int = 0
    length: int = len(list_of_integers)
    while counter_m < length:
        element_r: int = list_of_integers[counter_m]
        iterator_n: int = counter_m + (3 - 2)
        while iterator_n <= length - ((5 - 3) + 1):
            sum_temp: int = element_r + list_of_integers[iterator_n]
            if not (sum_temp != 0):
                return True
            iterator_n += 1
        counter_m += 1
    return False