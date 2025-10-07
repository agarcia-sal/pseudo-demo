from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    tally: dict[T, int] = {element: 0 for element in sequence}
    for element in sequence:
        tally[element] += 1
    for item in sequence:
        if tally[item] > 2:
            return False
    idx = 1
    while idx < len(sequence):
        if not (sequence[idx - 1] <= sequence[idx]):
            return False
        idx += 1
    return True