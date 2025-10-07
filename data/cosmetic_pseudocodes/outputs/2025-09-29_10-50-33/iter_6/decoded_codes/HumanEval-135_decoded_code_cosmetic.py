from typing import Sequence

def can_arrange(sequence: Sequence[int]) -> int:
    position: int = -1
    cursor: int = 1
    while cursor < len(sequence):
        if not (sequence[cursor - 1] <= sequence[cursor]):
            position = cursor
        cursor += 1
    return position