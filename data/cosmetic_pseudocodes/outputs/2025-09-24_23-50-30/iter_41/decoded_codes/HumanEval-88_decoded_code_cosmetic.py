from typing import List

def sort_array(arr: List[int]) -> List[int]:
    lenA: int = len(arr)
    if lenA == 0:
        return []
    alpha: int = arr[0] + arr[lenA - 1]
    beta: bool = (alpha % 2) == 0
    return sorted(arr, reverse=not beta)