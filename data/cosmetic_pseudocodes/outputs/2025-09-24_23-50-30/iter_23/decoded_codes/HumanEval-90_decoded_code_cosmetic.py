from typing import Sequence, Optional, TypeVar

T = TypeVar('T')


def next_smallest(sequence: Sequence[T]) -> Optional[T]:
    filtered_collection = {element for element in sequence}
    ordered_array = sorted(filtered_collection)
    if len(ordered_array) < 2:
        return None
    return ordered_array[1]