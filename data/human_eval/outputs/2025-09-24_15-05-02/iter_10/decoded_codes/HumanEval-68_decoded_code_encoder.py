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
    smallest_even = evens[0]
    for even_value in evens:
        if even_value < smallest_even:
            smallest_even = even_value
    index_of_smallest_even = 0
    for i in range(len(arr)):
        if arr[i] == smallest_even:
            index_of_smallest_even = i
            break
    return [smallest_even, index_of_smallest_even]