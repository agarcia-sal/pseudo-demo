from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessEqual')

class SupportsLessEqual:
    def __le__(self: T, other: T) -> bool: ...
    def __hash__(self) -> int: ...

def is_sorted(sequence: Sequence[T]) -> bool:
    tracker: dict[T, int] = {}
    for element in sequence:
        tracker[element] = tracker.get(element, 0) + 1
    for element in sequence:
        if tracker[element] > 2:
            return False
    index = 1
    while index < len(sequence):
        if not sequence[index - 1] <= sequence[index]:
            return False
        index += 1
    return True