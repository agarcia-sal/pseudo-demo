from typing import List

def sort_even(array_input: List[int]) -> List[int]:
    evens: List[int] = []
    odds: List[int] = []
    position: int = 0
    while position < len(array_input):
        if position % 2 == 0:
            evens.append(array_input[position])
        else:
            odds.append(array_input[position])
        position += 1
    evens.sort()  # sort evens in non-decreasing order

    combined_result: List[int] = []
    idx: int = 0
    while idx < len(odds):
        combined_result.append(evens[idx])
        combined_result.append(odds[idx])
        idx += 1

    if len(evens) > len(odds):
        combined_result.append(evens[-1])

    return combined_result