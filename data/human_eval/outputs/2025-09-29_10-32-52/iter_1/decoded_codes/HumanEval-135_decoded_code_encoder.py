from typing import List

def can_arrange(array: List[int]) -> int:
    index: int = -1
    iterator: int = 1
    length: int = len(array)
    while iterator < length:
        if array[iterator] < array[iterator - 1]:
            index = iterator
        iterator += 1
    return index