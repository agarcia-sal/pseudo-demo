from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool: ...
    def __eq__(self: T, other: T) -> bool: ...

def unique(list_of_elements: List[T]) -> List[T]:
    element_set = set(list_of_elements)
    sorted_unique_list = list(element_set)
    sorted_unique_list.sort()
    return sorted_unique_list