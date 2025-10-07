from typing import List, TypeVar, Callable, Union

T = TypeVar('T', bound=Union[int, float]]

def median(list_of_elements: List[T]) -> float:
    sorted_list = sorted(list_of_elements)  # sort elements
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_list[mid])  # middle element for odd length
    else:
        # average two middle elements for even length
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2