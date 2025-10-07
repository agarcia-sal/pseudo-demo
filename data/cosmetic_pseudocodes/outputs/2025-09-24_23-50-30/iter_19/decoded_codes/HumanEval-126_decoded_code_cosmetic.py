from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    tally: dict[T, int] = {}
    for element in sequence:
        tally[element] = 0
    for key in sequence:
        tally[key] += 1
    if any(value > 2 for value in (tally[x] for x in sequence)):
        return False
    for index in range(2, len(sequence)):
        if not (sequence[index - 1] <= sequence[index]):
            return False
    return True