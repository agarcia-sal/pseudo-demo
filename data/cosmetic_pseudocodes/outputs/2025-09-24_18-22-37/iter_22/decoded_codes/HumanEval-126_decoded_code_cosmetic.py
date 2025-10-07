from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessEqual')

class SupportsLessEqual:
    def __le__(self: T, other: T) -> bool:
        ...

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {key: 0 for key in sequence}
    idx: int = 0
    while idx < len(sequence):
        current_val = sequence[idx]
        temp_freq = frequency_map[current_val]
        frequency_map[current_val] = temp_freq + 1
        idx += 1
    violation_found: bool = False
    iterator_val: int = 0
    while iterator_val < len(sequence):
        if frequency_map[sequence[iterator_val]] > 2:
            violation_found = True
            break
        iterator_val += 1
    if violation_found:
        return False
    position: int = 1
    while True:
        if position >= len(sequence):
            break
        if not (sequence[position - 1] <= sequence[position]):
            return False
        position += 1
    return True