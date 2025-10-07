from typing import List

def sort_even(arr: List[int]) -> List[int]:
    evens: List[int] = []
    odds: List[int] = []
    idx: int = 0
    while idx < len(arr):
        if idx % 2 == 0:
            evens.append(arr[idx])
        else:
            odds.append(arr[idx])
        idx += 1

    evens.sort()

    result: List[int] = []
    position: int = 0
    while position < len(odds):
        result.append(evens[position])
        result.append(odds[position])
        position += 1

    if len(evens) > len(odds):
        result.append(evens[-1])

    return result