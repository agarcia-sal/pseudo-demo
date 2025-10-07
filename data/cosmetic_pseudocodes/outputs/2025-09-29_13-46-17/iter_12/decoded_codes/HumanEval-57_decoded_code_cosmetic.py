from typing import List, TypeVar

T = TypeVar("T")

def monotonic(list_of_elements: List[T]) -> bool:
    sorted_asc = sorted(list_of_elements)
    sorted_desc = sorted(list_of_elements, reverse=True)
    return list_of_elements == sorted_asc or list_of_elements == sorted_desc