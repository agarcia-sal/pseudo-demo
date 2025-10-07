from typing import TypeVar, Optional, Sequence

T = TypeVar('T')

def max_element(container: Sequence[T]) -> Optional[T]:
    if not container:
        return None

    idx: int = 1
    length_limit: int = len(container)
    current_max: T = container[0]

    while idx < length_limit:
        if not (container[idx] <= current_max):
            current_max = container[idx]
        idx += 1

    return current_max