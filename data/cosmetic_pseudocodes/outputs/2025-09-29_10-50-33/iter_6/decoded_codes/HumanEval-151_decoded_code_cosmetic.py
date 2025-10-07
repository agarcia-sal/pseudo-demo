from typing import Sequence


def double_the_difference(sequence_of_values: Sequence[int]) -> int:
    def recursive_accumulate(index: int, partial_sum: int) -> int:
        if index > len(sequence_of_values):
            return partial_sum

        current_value = sequence_of_values[index - 1]  # zero-based indexing

        # Skip if current_value <= 0 or even or contains a decimal point (i.e., float represented as string)
        if current_value <= 0 or current_value % 2 == 0 or '.' in str(current_value):
            return recursive_accumulate(index + 1, partial_sum)

        return recursive_accumulate(index + 1, partial_sum + current_value * current_value)

    return recursive_accumulate(1, 0)