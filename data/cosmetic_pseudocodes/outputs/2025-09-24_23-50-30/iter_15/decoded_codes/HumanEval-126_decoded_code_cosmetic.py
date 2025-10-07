from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T', bound=object)

def is_sorted(sequence: Sequence[T]) -> bool:
    frequencies: dict[T, int] = {}
    idx: int = 0
    length = len(sequence)

    while idx < length:
        temp_val = sequence[idx]
        frequencies[temp_val] = frequencies.get(temp_val, 0) + 1
        idx += 1

    for elem in sequence:
        if frequencies[elem] > 2:
            return False

    pos = 1
    while pos < length:
        if sequence[pos - 1] > sequence[pos]:
            return False
        pos += 1

    return True