from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    unique_items: List[T] = []
    for element in list_of_elements:
        if element not in unique_items:
            unique_items.append(element)
    return sorted(unique_items)