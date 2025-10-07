from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    total: int = array[0] + array[-1]
    descending: bool = (total % 2 == 0)
    result: List[int] = array[:]
    result.sort(reverse=descending)
    return result