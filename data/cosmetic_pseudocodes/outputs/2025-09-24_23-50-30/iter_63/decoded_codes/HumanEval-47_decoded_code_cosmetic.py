from typing import List, Union, TypeVar

T = TypeVar('T', int, float)

def median(list_of_elements: List[T]) -> float:
    temp_collection = sorted(list_of_elements)
    size = len(temp_collection)
    if size == 0:
        raise ValueError("median() arg is an empty list")
    if size % 2 == 1:
        # Odd number of elements: return the middle one as float
        return float(temp_collection[(size - 1) // 2])
    else:
        # Even number of elements: average the two middle elements
        lower_index = (size // 2) - 1
        upper_index = size // 2
        sum_val = temp_collection[lower_index] + temp_collection[upper_index]
        return sum_val * 0.5