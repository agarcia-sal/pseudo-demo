from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    temp_ascendant = sorted(list_of_elements)
    temp_descendant = sorted(list_of_elements, reverse=True)
    if list_of_elements != temp_ascendant and list_of_elements != temp_descendant:
        return False
    return True