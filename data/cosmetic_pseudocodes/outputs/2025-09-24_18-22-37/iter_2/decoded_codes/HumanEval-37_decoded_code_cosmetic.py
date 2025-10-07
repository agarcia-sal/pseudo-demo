from typing import List

def sort_even(arr: List[int]) -> List[int]:
    evens: List[int] = [arr[i] for i in range(0, len(arr), 2)]
    odds: List[int] = [arr[j] for j in range(1, len(arr), 2)]
    evens.sort()
    result: List[int] = []
    idx = 0
    while idx < len(odds):
        result.append(evens[idx])
        result.append(odds[idx])
        idx += 1
    if len(evens) > len(odds):
        result.append(evens[-1])
    return result