from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for item in sequence:
        frequency_map[item] = frequency_map.get(item, 0) + 1
    if any(frequency_map[element] > 2 for element in sequence):
        return False
    for idx in range(1, len(sequence)):
        if sequence[idx - 1] > sequence[idx]:
            return False
    return True