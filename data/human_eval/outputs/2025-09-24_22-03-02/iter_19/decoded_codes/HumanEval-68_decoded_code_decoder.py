from typing import List

def pluck(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        return []
    evens = [element for element in arr if element % 2 == 0]
    if len(evens) == 0:
        return []
    smallest_value = min(evens)
    smallest_index = next(index for index, element in enumerate(arr) if element == smallest_value)
    return [smallest_value, smallest_index]