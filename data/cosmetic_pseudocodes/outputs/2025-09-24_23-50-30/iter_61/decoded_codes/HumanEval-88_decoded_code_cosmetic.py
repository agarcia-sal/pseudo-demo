from typing import List

def sort_array(qwerty: List[int]) -> List[int]:
    length = len(qwerty)
    if length == 0:
        return []
    asdfg = qwerty[0] + qwerty[length - 1]
    zxcvb = (asdfg % 2 == 0)  # True if sum is even, False if odd
    return sorted(qwerty, reverse=zxcvb)