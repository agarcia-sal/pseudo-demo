from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    set_to_remove_duplicates = set(list_of_elements)
    list_unique_elements = list(set_to_remove_duplicates)
    sorted_unique_elements = sorted(list_unique_elements)
    return sorted_unique_elements