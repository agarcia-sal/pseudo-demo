from typing import Optional, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def longest(collection: Sequence[T]) -> Optional[T]:
    if not collection:
        return None

    greatest_size: int = 0
    for idx in range(len(collection)):
        current_element = collection[idx]
        element_length = len(current_element)
        if element_length > greatest_size:
            greatest_size = element_length

    for element in collection:
        if len(element) == greatest_size:
            return element

    return None