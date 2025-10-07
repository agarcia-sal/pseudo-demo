from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = -1
    for idx in range(len(list_of_integers)):
        if list_of_integers[idx] > max_val:
            max_val = list_of_integers[idx]

    count_array: List[int] = [0] * (max_val + 1) if max_val >= 0 else []

    pos: int = 0
    while pos < len(list_of_integers):
        element: int = list_of_integers[pos]
        count_array[element] += 1
        pos += 1

    result: int = -1
    pointer: int = 1
    while pointer < len(count_array):
        if not (count_array[pointer] < pointer):
            result = pointer
        pointer += 1

    return result