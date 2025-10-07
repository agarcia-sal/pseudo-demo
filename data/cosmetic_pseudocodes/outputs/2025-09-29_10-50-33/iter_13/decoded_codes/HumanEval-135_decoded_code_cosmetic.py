from typing import List, Optional


def can_arrange(array: List[int]) -> Optional[int]:
    index_marker: int = -1
    cursor: int = 1
    while True:
        if cursor >= len(array):
            return index_marker
        if array[cursor] < array[cursor - 1]:
            index_marker = cursor
        cursor += 1