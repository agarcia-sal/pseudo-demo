from typing import List

def pluck(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        return []

    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return []

    smallest_even_value = min(evens)
    smallest_even_index = arr.index(smallest_even_value)

    return [smallest_even_value, smallest_even_index]