from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    tracker: dict[T, int] = {}
    for element in sequence:
        tracker[element] = tracker.get(element, 0) + 1
    if any(count > 2 for count in tracker.values()):
        return False
    idx = 1
    while idx < len(sequence):
        if sequence[idx - 1] > sequence[idx]:
            return False
        idx += 1
    return True