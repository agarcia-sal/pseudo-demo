from typing import List, Union

def pluck(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    evens = [element for element in array if element % 2 == 0]
    if len(evens) == 0:
        return []
    smallest_even = min(evens)
    index_of_smallest_even = array.index(smallest_even)
    return [smallest_even, index_of_smallest_even]