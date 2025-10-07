from typing import List


def get_positive(sequence_of_values: List[int]) -> List[int]:
    def helper(index: int, accumulator: List[int]) -> List[int]:
        if index >= len(sequence_of_values):
            return accumulator
        value = sequence_of_values[index]
        new_accumulator = accumulator + [value] if value > 0 else accumulator
        return helper(index + 1, new_accumulator)

    return helper(0, [])