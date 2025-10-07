from typing import Sequence, List


def get_positive(sequence_of_values: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(sequence_of_values):
        if sequence_of_values[iterator_index] > 0:
            accumulator.append(sequence_of_values[iterator_index])
        iterator_index += 1

    return accumulator