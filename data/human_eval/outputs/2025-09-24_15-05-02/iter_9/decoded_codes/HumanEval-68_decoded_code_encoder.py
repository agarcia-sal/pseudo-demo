from typing import List, Union

def pluck(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        return []
    evens = [element for element in arr if element % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)
    return [smallest_even, smallest_index]