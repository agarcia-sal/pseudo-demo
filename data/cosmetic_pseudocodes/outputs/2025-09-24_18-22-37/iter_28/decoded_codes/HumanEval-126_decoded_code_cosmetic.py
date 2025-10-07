from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    freq_map: dict[T, int] = {elem: 0 for elem in sequence}
    idx_outer: int = 0
    while idx_outer < len(sequence):
        current_val = sequence[idx_outer]
        freq_map[current_val] += 1
        idx_outer += 1

    has_excess_duplicates = any(count > 2 for count in freq_map.values())
    if has_excess_duplicates:
        return False

    sorted_flag = True
    pos = 1
    while pos < len(sequence) - 1:
        if sequence[pos - 1] > sequence[pos]:
            sorted_flag = False
            break
        pos += 1

    if sorted_flag:
        return True
    else:
        return False