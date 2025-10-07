from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    ascending_flag: bool = list_of_elements == sorted(list_of_elements)
    descending_flag: bool = list_of_elements == sorted(list_of_elements, reverse=True)
    return ascending_flag or descending_flag