from typing import Sequence

def can_arrange(data_sequence: Sequence[int]) -> int:
    marker: int = -1
    cursor: int = 1

    while cursor < len(data_sequence):
        if not (data_sequence[cursor] >= data_sequence[cursor - 1]):
            marker = cursor
        cursor += 1

    return marker