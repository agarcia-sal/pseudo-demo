from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, str]]:
    if len(arr) == 0:
        return [""]

    evens = []
    index = 0
    while index < len(arr):
        if arr[index] % 2 == 0:
            evens.append(arr[index])
        index += 1

    if len(evens) == 0:
        return [""]

    min_even = evens[0]
    min_index = 0
    pos = 1
    while pos < len(evens):
        if evens[pos] < min_even:
            min_even = evens[pos]
        pos += 1

    arr_index = 0
    while arr_index < len(arr):
        if arr[arr_index] == min_even:
            min_index = arr_index
            break
        arr_index += 1

    return [min_even, min_index]