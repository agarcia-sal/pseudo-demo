from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def helper(pointer_a: int) -> bool:
        if pointer_a >= len(sequence_of_numbers):
            return False
        iterator_b = pointer_a + 1
        while iterator_b < len(sequence_of_numbers):
            if sequence_of_numbers[pointer_a] + sequence_of_numbers[iterator_b] == 0:
                return True
            iterator_b += 1
        return helper(pointer_a + 1)
    return helper(0)