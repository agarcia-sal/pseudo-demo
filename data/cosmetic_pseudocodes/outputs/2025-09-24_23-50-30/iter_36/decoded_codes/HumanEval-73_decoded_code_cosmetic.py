from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    count_difference: int = 0
    limit: int = (len(sequence_of_numbers) // 2) - 1

    def increment_if_mismatch(position: int) -> None:
        nonlocal count_difference
        if position > limit:
            return
        if sequence_of_numbers[position] != sequence_of_numbers[len(sequence_of_numbers) - position - 1]:
            count_difference += 1
        increment_if_mismatch(position + 1)

    increment_if_mismatch(0)
    return count_difference