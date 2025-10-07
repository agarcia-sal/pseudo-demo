from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    ascending_check = True
    descending_check = True

    for index in range(1, len(list_of_elements)):
        if list_of_elements[index] < list_of_elements[index - 1]:
            ascending_check = False
        if list_of_elements[index] > list_of_elements[index - 1]:
            descending_check = False

    return ascending_check or descending_check