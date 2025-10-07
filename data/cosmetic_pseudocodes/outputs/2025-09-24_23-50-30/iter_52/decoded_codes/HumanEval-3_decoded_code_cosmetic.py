from typing import Sequence

def below_zero(sequence_of_changes: Sequence[int]) -> bool:
    def traverse(index: int, accumulator: int) -> bool:
        if index >= len(sequence_of_changes):
            return False
        elif accumulator + sequence_of_changes[index] < 0:
            return True
        else:
            return traverse(index + 1, accumulator + sequence_of_changes[index])
    return traverse(0, 0)