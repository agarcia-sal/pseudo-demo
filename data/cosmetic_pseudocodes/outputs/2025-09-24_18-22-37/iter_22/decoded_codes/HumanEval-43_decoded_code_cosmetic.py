from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    pos: int = 0
    length: int = len(sequence_of_numbers)
    while pos < length:
        val_a: int = sequence_of_numbers[pos]
        next_pos: int = pos + 1
        while next_pos <= length - 1:
            val_b: int = sequence_of_numbers[next_pos]
            combined_sum: int = val_a + val_b
            if combined_sum == 0:
                return True
            else:
                next_pos += 1
        pos += 1
    return False