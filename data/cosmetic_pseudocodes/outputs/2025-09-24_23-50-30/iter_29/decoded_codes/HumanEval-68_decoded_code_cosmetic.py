from typing import List, Union

def pluck(list_of_items: List[int]) -> List[Union[int, int]]:
    if len(list_of_items) == 0:
        return []
    evens = [x for x in list_of_items if x % 2 == 0]
    if len(evens) == 0:
        return []
    min_even = evens[0]
    for y in evens:
        if y < min_even:
            min_even = y
    idx = 0
    while idx < len(list_of_items):
        if list_of_items[idx] == min_even:
            break
        idx += 1
    return [min_even, idx]