from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, int]]:
    if len(arr) == 0:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return []
    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)
    return [smallest_even, smallest_index]