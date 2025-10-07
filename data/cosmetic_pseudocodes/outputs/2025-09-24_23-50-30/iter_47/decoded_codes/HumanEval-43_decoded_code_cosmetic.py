from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    index_primary: int = 0
    length: int = len(sequence_of_numbers)
    while index_primary < length:
        value_primary: int = sequence_of_numbers[index_primary]
        index_secondary: int = index_primary + 1
        while index_secondary < length:
            value_secondary: int = sequence_of_numbers[index_secondary]
            if not (value_primary + value_secondary != 0):
                return True
            index_secondary += 1
        index_primary += 1
    return False