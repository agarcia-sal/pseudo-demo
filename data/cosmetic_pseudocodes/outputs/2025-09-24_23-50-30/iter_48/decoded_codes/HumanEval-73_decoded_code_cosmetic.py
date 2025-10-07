from typing import Sequence


def smallest_change(sequence: Sequence) -> int:
    count: int = 0
    length: int = len(sequence)
    half_length: int = (length - (length % 2)) // 2
    position: int = 0
    while position < half_length:
        if sequence[position] != sequence[length - (position + 1)]:
            count += 1
        position += 1
    return count