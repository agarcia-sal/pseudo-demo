from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, int]]:
    if len(arr) == 0:
        return []
    evens = []
    for element in arr:
        if element % 2 == 0:
            evens.append(element)
    if len(evens) == 0:
        return []
    minimum_even = min(evens)
    index_of_minimum = arr.index(minimum_even)
    return [minimum_even, index_of_minimum]