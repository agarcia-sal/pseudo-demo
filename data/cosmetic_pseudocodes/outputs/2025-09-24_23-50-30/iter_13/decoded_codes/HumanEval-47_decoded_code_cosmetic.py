from typing import List, TypeVar, Union
from math import floor

T = TypeVar('T', int, float)

def median(list_of_elements: List[T]) -> Union[T, float]:
    sorted_elements: List[T] = []
    for item in list_of_elements:
        sorted_elements.append(item)
    sorted_elements.sort()
    count: int = len(sorted_elements)
    middle_index: float = count / 2
    if count % 2 != 0:
        return sorted_elements[floor(middle_index)]  # middle element for odd count
    first_mid_val: T = sorted_elements[int(middle_index) - 1]
    second_mid_val: T = sorted_elements[int(middle_index)]
    return (first_mid_val + second_mid_val) / 2.0  # average for even count