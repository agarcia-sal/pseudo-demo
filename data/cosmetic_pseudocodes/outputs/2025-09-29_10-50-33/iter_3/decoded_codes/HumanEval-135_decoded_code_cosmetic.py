from typing import Sequence

def can_arrange(collection: Sequence[int]) -> int:
    marker: int = -1
    cursor: int = 1

    while cursor < len(collection):
        if collection[cursor] < collection[cursor - 1]:
            marker = cursor
        cursor += 1

    return marker