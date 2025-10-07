from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')


def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for element in sequence:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    if any(count > 2 for count in frequency_map.values()):
        return False

    for i in range(1, len(sequence)):
        if sequence[i] < sequence[i - 1]:
            return False

    return True