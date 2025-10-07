from typing import Sequence


def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    iterator_m: int = 0
    length: int = len(sequence_of_numbers)
    while iterator_m < length:
        value_u: int = sequence_of_numbers[iterator_m]
        iterator_n: int = iterator_m + 1
        while iterator_n < length:
            value_v: int = sequence_of_numbers[iterator_n]
            combined_sum: int = value_u + value_v
            if combined_sum == 0:
                return True
            iterator_n += 1
        iterator_m += 1
    return False