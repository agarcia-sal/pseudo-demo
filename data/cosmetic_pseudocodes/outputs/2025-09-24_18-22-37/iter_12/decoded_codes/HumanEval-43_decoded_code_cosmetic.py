from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length: int = len(sequence_of_numbers)
    for iterator_k in range(length):
        value_m: int = sequence_of_numbers[iterator_k]
        for iterator_n in range(iterator_k + 1, length):
            value_p: int = sequence_of_numbers[iterator_n]
            sum_result: int = value_m + value_p
            if not (sum_result != 0):  # sum_result == 0
                return True
    return False