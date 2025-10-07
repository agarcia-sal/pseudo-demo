from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    def sum_helper(index: int, accumulator: int) -> int:
        if index > len(sequence_of_numbers):
            return accumulator
        value = sequence_of_numbers[index - 1]  # Adjust for 0-based indexing
        new_accumulator = accumulator + (value if value % 2 == 0 else 0)
        return sum_helper(index + 2, new_accumulator)
    return sum_helper(1, 0)