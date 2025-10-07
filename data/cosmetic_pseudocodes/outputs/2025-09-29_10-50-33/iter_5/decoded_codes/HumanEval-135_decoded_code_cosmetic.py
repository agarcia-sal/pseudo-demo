from typing import List

def can_arrange(sequence: List[int]) -> int:
    positionIndicator: int = -1
    cursor: int = 1

    while cursor < len(sequence):
        if sequence[cursor] < sequence[cursor - 1]:
            positionIndicator = cursor
        cursor += 1

    return positionIndicator