from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, List]]:
    if len(arr) == 0:
        return ["empty"]

    evens = [element for element in arr if element % 2 == 0]

    if len(evens) == 0:
        return ["empty"]

    minimum_even = evens[0]
    for element in evens:
        if element < minimum_even:
            minimum_even = element

    index_of_minimum_even = -1
    for index in range(len(arr)):
        if arr[index] == minimum_even:
            index_of_minimum_even = index
            break

    return [minimum_even, index_of_minimum_even]