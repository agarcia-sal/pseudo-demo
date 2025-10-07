from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...

def monotonic(list_of_elements: List[T]) -> bool:
    ascending_flag = True
    descending_flag = True

    index = 0
    while index < len(list_of_elements) - 1:
        if list_of_elements[index] > list_of_elements[index + 1]:
            ascending_flag = False
        if list_of_elements[index] < list_of_elements[index + 1]:
            descending_flag = False
        index += 1

    return ascending_flag or descending_flag