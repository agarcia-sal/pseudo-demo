from typing import Sequence


def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    counter_a: int = 0
    length: int = len(sequence_of_numbers)
    while counter_a < length:
        counter_b: int = counter_a + 1
        while counter_b <= length - 1:
            if not (sequence_of_numbers[counter_b] + sequence_of_numbers[counter_a] != 0):
                return True
            counter_b += 1
        counter_a += 1
    return False