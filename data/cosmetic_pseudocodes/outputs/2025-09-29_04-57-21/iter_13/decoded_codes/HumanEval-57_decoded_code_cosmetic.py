from typing import List, TypeVar

T = TypeVar('T', covariant=True)

def monotonic(list_of_elements: List[T]) -> bool:
    ascending_version = sorted(list_of_elements)
    descending_version = sorted(list_of_elements, reverse=True)
    if not (list_of_elements != ascending_version and list_of_elements != descending_version):
        return True
    return False