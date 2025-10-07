from typing import Sequence, List, Optional


def pluck(sequence: Sequence[int]) -> List[int]:
    result: List[int] = []
    filtered: List[int] = []
    idx: int = 0
    smallest_val: Optional[int] = None
    smallest_idx: Optional[int] = None

    while idx < len(sequence):
        if not (sequence[idx] % 2 != 0):  # select even numbers
            filtered.append(sequence[idx])
        idx += 1

    if len(filtered) == 0:
        return result

    smallest_val = filtered[0]
    idx = 0
    while idx < len(filtered):
        if filtered[idx] < smallest_val:
            smallest_val = filtered[idx]
        idx += 1

    smallest_idx = 0
    idx = 0
    while idx < len(sequence):
        if sequence[idx] == smallest_val:
            smallest_idx = idx
            break
        idx += 1

    result = [smallest_val, smallest_idx]
    return result