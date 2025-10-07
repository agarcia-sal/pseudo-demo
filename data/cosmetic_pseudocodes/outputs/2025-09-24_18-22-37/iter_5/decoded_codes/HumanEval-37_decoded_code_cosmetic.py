from typing import List

def sort_even(input_array: List[int]) -> List[int]:
    evens: List[int] = []
    odds: List[int] = []
    idx: int = 0
    while idx < len(input_array):
        evens.append(input_array[idx])
        idx += 2

    idx = 1
    while idx < len(input_array):
        odds.append(input_array[idx])
        idx += 2

    evens.sort()

    result: List[int] = []
    position: int = 0
    while position < len(odds) and position < len(evens):
        result.append(evens[position])
        result.append(odds[position])
        position += 1

    if len(evens) > len(odds):
        result.append(evens[-1])

    return result