from typing import Sequence


def below_zero(sequence_of_increments: Sequence[int]) -> bool:
    accumulator = 0
    for index in range(len(sequence_of_increments)):
        accumulator += sequence_of_increments[index]
        if accumulator < 0:
            return True
    return False