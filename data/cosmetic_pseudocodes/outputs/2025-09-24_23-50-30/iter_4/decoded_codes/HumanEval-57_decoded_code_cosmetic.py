from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

# Define a protocol for types that support comparison operators
class Comparable:
    def __ge__(self: T, other: T) -> bool: ...
    def __le__(self: T, other: T) -> bool: ...

def monotonic(list_of_elements: List[T]) -> bool:
    asc_sorted = True
    desc_sorted = True
    for i in range(1, len(list_of_elements)):
        asc_sorted = asc_sorted and (list_of_elements[i] >= list_of_elements[i - 1])
        desc_sorted = desc_sorted and (list_of_elements[i] <= list_of_elements[i - 1])
    return asc_sorted or desc_sorted