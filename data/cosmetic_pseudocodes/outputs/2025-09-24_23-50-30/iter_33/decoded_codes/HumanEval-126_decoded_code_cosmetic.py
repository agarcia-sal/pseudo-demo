from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {key: 0 for key in sequence}
    index_var: int = 0
    length: int = len(sequence)
    while index_var < length:
        frequency_map[sequence[index_var]] += 1
        index_var += 1
    for key in frequency_map:
        if frequency_map[key] > 2:
            return False
    pos: int = 1
    is_non_decreasing: bool = True
    while pos < length and is_non_decreasing:
        is_non_decreasing = (sequence[pos - 1] <= sequence[pos]) and is_non_decreasing
        pos += 1
    return is_non_decreasing