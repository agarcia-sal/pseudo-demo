from typing import Sequence

def pairs_sum_to_zero(numbers_array: Sequence[int]) -> bool:
    length_tmp: int = len(numbers_array)
    iterator_m: int = 0
    while iterator_m < length_tmp:
        value_m: int = numbers_array[iterator_m]
        iterator_n: int = iterator_m + 1
        while iterator_n < length_tmp:
            value_n: int = numbers_array[iterator_n]
            sum_tmp: int = value_m + value_n
            if sum_tmp == 0:
                return True
            else:
                iterator_n += 1
        iterator_m += 1
    return False