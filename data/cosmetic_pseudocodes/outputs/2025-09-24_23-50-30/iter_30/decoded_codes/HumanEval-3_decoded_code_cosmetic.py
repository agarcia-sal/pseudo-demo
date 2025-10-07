from typing import Sequence


def below_zero(sequence_of_values: Sequence[int]) -> bool:
    aggregate = 0
    index = 0

    while index < len(sequence_of_values):
        aggregate += sequence_of_values[index]
        if aggregate >= 0:
            index += 1
        else:
            return True

    return False