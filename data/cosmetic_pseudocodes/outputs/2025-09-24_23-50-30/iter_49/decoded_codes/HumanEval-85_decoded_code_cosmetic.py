from typing import Sequence


def add(sequence_of_numbers: Sequence[int]) -> int:
    def auxiliary(accumulator: int, current_index: int) -> int:
        if not (current_index < len(sequence_of_numbers)):
            return accumulator
        return auxiliary(
            accumulator + (sequence_of_numbers[current_index] if sequence_of_numbers[current_index] % 2 == 0 else 0),
            current_index + 2,
        )
    return auxiliary(0, 1)