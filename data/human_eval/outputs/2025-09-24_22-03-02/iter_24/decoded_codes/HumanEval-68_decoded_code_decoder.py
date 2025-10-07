from typing import List, Union

def pluck(arr: List[int]) -> Union[List[int], List[Union[int, int]]]:
    if len(arr) == 0:
        return []

    evens = []
    index = 0
    while index < len(arr):
        element = arr[index]
        if element % 2 == 0:
            evens.append(element)
        index += 1

    if len(evens) == 0:
        return []

    minimum_even = evens[0]
    index_evens = 1
    while index_evens < len(evens):
        if evens[index_evens] < minimum_even:
            minimum_even = evens[index_evens]
        index_evens += 1

    min_index = 0
    index_arr = 0
    while index_arr < len(arr):
        if arr[index_arr] == minimum_even:
            min_index = index_arr
            break
        index_arr += 1

    return [minimum_even, min_index]