from typing import List

def derivative(arr: List[int]) -> List[int]:
    result: List[int] = []
    i: int = 1
    while i < len(arr):
        result.append(arr[i] * i)
        i += 1
    return result