from typing import Sequence, List

def get_positive(sequence: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index < len(sequence):
        if not (sequence[index] <= 0):
            accumulator.append(sequence[index])
        index += 1
    return accumulator