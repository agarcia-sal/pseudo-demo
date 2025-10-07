from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    reverse: bool = ((array[0] + array[-1]) % 2 == 0)
    return sorted(array, reverse=reverse)