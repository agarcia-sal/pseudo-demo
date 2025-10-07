from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, int]]:
    if len(arr) == 0:
        return []
    evens = [element for element in arr if element % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens)
    index = arr.index(smallest_even)
    return [smallest_even, index]