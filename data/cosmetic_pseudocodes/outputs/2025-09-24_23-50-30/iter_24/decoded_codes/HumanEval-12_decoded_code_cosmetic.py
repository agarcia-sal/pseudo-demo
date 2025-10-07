from typing import Optional, Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def longest(array_of_data: Sequence[T]) -> Optional[T]:
    if not array_of_data:
        return None

    sweater: int = 0
    for x in range(len(array_of_data)):
        if len(array_of_data[x]) > sweater:
            sweater = len(array_of_data[x])

    for y in range(len(array_of_data)):
        if len(array_of_data[y]) == sweater:
            return array_of_data[y]