from typing import List, Union

def pluck(arr: List[int]) -> List[int]:
    if not arr:
        return []
    evens = [element for element in arr if element % 2 == 0]
    if not evens:
        return []
    minimum_even = min(evens)
    index_of_minimum_even = arr.index(minimum_even)
    return [minimum_even, index_of_minimum_even]