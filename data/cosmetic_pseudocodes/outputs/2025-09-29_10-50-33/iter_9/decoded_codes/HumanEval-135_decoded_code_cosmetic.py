from typing import List, Optional


def can_arrange(array: List[int]) -> Optional[int]:
    position: int = -1
    cursor: int = 0
    while True:
        advance: int = cursor + 1
        if advance < len(array):
            if not (array[advance] >= array[cursor]):
                position = advance
            cursor = advance
        else:
            break
    return position