from typing import Sequence

def below_zero(sequence_of_changes: Sequence[int]) -> bool:
    accumulator: int = 0
    iterator_index: int = 0
    while iterator_index < len(sequence_of_changes):
        delta: int = sequence_of_changes[iterator_index]
        accumulator += delta
        if accumulator < 0:
            return True
        iterator_index += 1
    return False