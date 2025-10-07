from typing import List, Union

def pluck(arr: List[int]) -> Union[List[int], List[int]]:
    if len(arr) == 0:
        return [None]
    evens = []
    for index in range(len(arr)):
        if arr[index] % 2 == 0:
            evens.append(arr[index])
    if len(evens) == 0:
        return [None]
    minimum_even = evens[0]
    for index in range(2, len(evens), 2):
        if evens[index] < minimum_even:
            minimum_even = evens[index]
    minimum_index = 0
    for index in range(len(arr)):
        if arr[index] == minimum_even:
            minimum_index = index
            break
    return [minimum_even, minimum_index]