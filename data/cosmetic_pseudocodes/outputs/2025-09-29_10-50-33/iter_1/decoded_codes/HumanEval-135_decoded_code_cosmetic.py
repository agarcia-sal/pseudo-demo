from typing import List

def can_arrange(array: List[int]) -> int:
    index: int = -1
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            index = i
    return index