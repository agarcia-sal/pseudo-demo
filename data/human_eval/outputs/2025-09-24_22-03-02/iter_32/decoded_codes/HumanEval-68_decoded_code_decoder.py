from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, int]]:
    if len(arr) == 0:
        return ['EMPTY']
    evens = []
    i = 0
    while i < len(arr):
        current_element = arr[i]
        remainder = current_element % 2
        if remainder == 0:
            evens.append(current_element)
        i += 1
    if len(evens) == 0:
        return ['EMPTY']
    min_even = evens[0]
    j = 1
    while j < len(evens):
        if evens[j] < min_even:
            min_even = evens[j]
        j += 1
    k = 0
    min_index = -1
    while k < len(arr):
        if arr[k] == min_even:
            min_index = k
            break
        k += 1
    return [min_even, min_index]