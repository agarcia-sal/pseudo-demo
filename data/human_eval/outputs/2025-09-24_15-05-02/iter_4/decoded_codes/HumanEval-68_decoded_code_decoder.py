from typing import List, Union

def pluck(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        return []

    evens = [value for value in arr if value % 2 == 0]

    if not evens:
        return []

    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)
    return [smallest_even, smallest_index]