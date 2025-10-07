from typing import List, TypeVar

T = TypeVar('T', bound=object)

def monotonic(list_of_elements: List[T]) -> bool:
    ascending_check: bool = list_of_elements == sorted(list_of_elements)
    descending_check: bool = list_of_elements == sorted(list_of_elements, reverse=True)
    return ascending_check or descending_check