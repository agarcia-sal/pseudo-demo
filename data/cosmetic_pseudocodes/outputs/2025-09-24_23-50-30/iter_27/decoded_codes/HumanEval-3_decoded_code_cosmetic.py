from typing import Sequence


def below_zero(sequence_of_moves: Sequence[int]) -> bool:
    accumulator: int = 0
    index: int = 0
    while index < len(sequence_of_moves):
        current_item: int = sequence_of_moves[index]
        accumulator += current_item
        if accumulator < 0:
            return True
        index += 1
    return False