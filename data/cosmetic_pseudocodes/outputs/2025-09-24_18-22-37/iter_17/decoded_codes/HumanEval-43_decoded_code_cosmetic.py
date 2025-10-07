from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    position_m = 0
    length = len(sequence_of_numbers)
    while position_m < length:
        value_a = sequence_of_numbers[position_m]
        position_n = position_m + 1
        while position_n < length:
            value_b = sequence_of_numbers[position_n]
            if value_a + value_b == 0:
                return True
            position_n += 1
        position_m += 1
    return False