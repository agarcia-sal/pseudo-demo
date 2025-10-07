from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int]]:
    if not arr:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)
    return [smallest_even, smallest_index]