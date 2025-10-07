from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    counter_a = 0
    length = len(sequence_of_numbers)
    while counter_a < length - 1:
        counter_b = counter_a + 1
        while counter_b < length:
            if sequence_of_numbers[counter_b] == -sequence_of_numbers[counter_a]:
                return True
            counter_b += 1
        counter_a += 1
    return False