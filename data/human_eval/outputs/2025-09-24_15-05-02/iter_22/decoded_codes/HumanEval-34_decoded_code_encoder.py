from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    unique_elements: List[T] = []
    seen_elements: set[T] = set()
    for element in list_of_elements:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.add(element)
    unique_elements.sort()
    return unique_elements