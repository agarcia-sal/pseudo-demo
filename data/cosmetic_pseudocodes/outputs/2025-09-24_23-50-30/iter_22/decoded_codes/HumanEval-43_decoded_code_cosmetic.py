from typing import Sequence


def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    for index_a in range(length - 1):
        for index_b in range(index_a + 1, length):
            if sequence_of_numbers[index_a] - (-sequence_of_numbers[index_b]) == 0:
                return True
    return False