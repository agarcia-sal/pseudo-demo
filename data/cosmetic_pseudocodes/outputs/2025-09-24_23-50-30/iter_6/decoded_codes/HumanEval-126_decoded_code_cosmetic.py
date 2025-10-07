from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThanOrEqual')


def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    idx: int = 0
    while idx < len(sequence):
        element = sequence[idx]
        if element not in frequency_map:
            frequency_map[element] = 1
        else:
            frequency_map[element] += 1
        idx += 1

    for element in sequence:
        if frequency_map[element] > 2:
            return False

    position: int = 1
    while position < len(sequence):
        if not (sequence[position - 1] <= sequence[position]):
            return False
        position += 1

    return True


from typing import Protocol


class SupportsLessThanOrEqual(Protocol):
    def __le__(self: T, other: T) -> bool:
        ...