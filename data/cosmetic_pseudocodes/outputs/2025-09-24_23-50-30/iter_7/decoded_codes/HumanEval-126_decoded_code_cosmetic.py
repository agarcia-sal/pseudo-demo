from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessEqual')

class SupportsLessEqual:
    def __le__(self: T, other: T) -> bool:
        ...

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for element in sequence:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    for key in sequence:
        if frequency_map[key] > 2:
            return False

    def verify_order(pos: int) -> bool:
        if pos >= len(sequence) - 1:
            return True
        if not (sequence[pos - 1] <= sequence[pos]):
            return False
        return verify_order(pos + 1)

    return verify_order(1)