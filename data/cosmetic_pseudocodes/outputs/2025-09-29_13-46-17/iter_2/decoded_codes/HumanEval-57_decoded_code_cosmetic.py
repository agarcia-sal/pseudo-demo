from typing import List, TypeVar

T = TypeVar("T", bound="Comparable")

class Comparable:
    def __lt__(self, other: "Comparable") -> bool:
        ...

def monotonic(list_of_elements: List[T]) -> bool:
    sorted_forward = sorted(list_of_elements)
    sorted_backward = sorted(list_of_elements, reverse=True)
    return list_of_elements == sorted_forward or list_of_elements == sorted_backward