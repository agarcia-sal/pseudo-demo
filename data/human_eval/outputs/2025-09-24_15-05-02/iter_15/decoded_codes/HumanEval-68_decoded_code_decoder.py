from typing import List, Union

def pluck(array: List[int]) -> List[Union[int, int]]:
    if len(array) == 0:
        return []
    evens = [x for x in array if x % 2 == 0]
    if len(evens) == 0:
        return []
    smallest_even = min(evens)
    smallest_index = array.index(smallest_even)
    return [smallest_even, smallest_index]