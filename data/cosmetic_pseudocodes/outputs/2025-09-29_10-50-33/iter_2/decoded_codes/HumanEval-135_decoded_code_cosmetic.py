from typing import List

def can_arrange(array: List[int]) -> int:
    marker: int = -1
    cursor: int = 1
    while cursor < len(array):
        if array[cursor] < array[cursor - 1]:
            marker = cursor
        cursor += 1
    return marker