from typing import List, Union

def pluck(arr: List[int]) -> Union[List[int], List]:
    if len(arr) == 0:
        return []
    evens = []
    for index in range(len(arr)):
        element = arr[index]
        if element % 2 == 0:
            evens.append(element)
    if len(evens) == 0:
        return []
    minimum_even = evens[0]
    for i in range(1, len(evens)):
        if evens[i] < minimum_even:
            minimum_even = evens[i]
    minimum_even_index = -1
    for j in range(len(arr)):
        if arr[j] == minimum_even:
            minimum_even_index = j
            break
    return [minimum_even, minimum_even_index]