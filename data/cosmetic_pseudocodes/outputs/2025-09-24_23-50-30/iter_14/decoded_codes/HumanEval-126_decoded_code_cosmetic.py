from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for element in sequence:
        frequency_map[element] = frequency_map.get(element, 0) + 1
    if any(count > 2 for count in frequency_map.values()):
        return False
    return all(sequence[idx] >= sequence[idx - 1] for idx in range(1, len(sequence)))