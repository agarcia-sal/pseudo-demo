from typing import Sequence

def pairs_sum_to_zero(collection_of_numbers: Sequence[int]) -> bool:
    position_m = 0
    length = len(collection_of_numbers)
    while position_m < length - 1:
        value_p = collection_of_numbers[position_m]
        position_n = position_m + 1
        while position_n < length:
            if value_p + collection_of_numbers[position_n] == 0:
                return True
            position_n += 1
        position_m += 1
    return False