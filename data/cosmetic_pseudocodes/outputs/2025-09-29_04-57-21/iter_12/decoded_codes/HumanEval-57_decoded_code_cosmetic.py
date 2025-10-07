from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool:
        ...


def monotonic(list_of_elements: List[T]) -> bool:
    ascending_check = list_of_elements == sorted(list_of_elements)
    descending_check = list_of_elements == sorted(list_of_elements, reverse=True)
    return ascending_check or descending_check