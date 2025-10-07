from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    total_count: int = len(list_of_integers)
    iterator_m: int = 0

    while iterator_m < total_count:
        current_value: int = list_of_integers[iterator_m]
        iterator_n: int = iterator_m + 1

        while iterator_n < total_count:
            candidate_value: int = list_of_integers[iterator_n]
            sum_temp: int = current_value + candidate_value
            if sum_temp == 0:
                return True
            iterator_n += 1

        iterator_m += 1

    return False