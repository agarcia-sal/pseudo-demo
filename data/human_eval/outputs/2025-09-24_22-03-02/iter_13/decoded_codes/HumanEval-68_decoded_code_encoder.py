from typing import List, Union

def pluck(arr: List[int]) -> List[Union[int, int]]:
    if len(arr) == 0:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return []
    minimum_even = min(evens)
    minimum_index = arr.index(minimum_even)
    return [minimum_even, minimum_index]