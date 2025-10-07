from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    ascending = True
    descending = True

    for i in range(1, len(list_of_elements)):
        if list_of_elements[i] < list_of_elements[i - 1]:
            ascending = False
        if list_of_elements[i] > list_of_elements[i - 1]:
            descending = False

    return ascending or descending