from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {element: 0 for element in sequence}

    idx = 0
    while idx < len(sequence):
        val = sequence[idx]
        frequency_map[val] += 1
        idx += 1

    limit_exceeded = False
    for element in sequence:
        if frequency_map[element] > 2:
            limit_exceeded = True
            break

    if limit_exceeded:
        return False

    position = 1
    ordered = True
    while position < len(sequence) and ordered:
        previous_val = sequence[position - 1]
        current_val = sequence[position]
        if previous_val > current_val:
            ordered = False
        position += 1

    if ordered:
        return True
    return False