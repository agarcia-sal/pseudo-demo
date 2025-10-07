from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=object)

def monotonic(list_of_elements: Sequence[T]) -> bool:
    ascending_versions: List[List[T]] = [sorted(list_of_elements), sorted(list_of_elements, reverse=True)]
    for each_version in ascending_versions:
        if list_of_elements == each_version:
            return True
    return False