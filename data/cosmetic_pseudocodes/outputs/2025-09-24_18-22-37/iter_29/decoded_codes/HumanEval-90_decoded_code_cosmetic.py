from typing import Optional, Sequence, TypeVar

T = TypeVar('T', bound=object)

def next_smallest(numbers_collection: Sequence[T]) -> Optional[T]:
    filtered_collection = list(dict.fromkeys(numbers_collection))  # remove duplicates while preserving order
    ordered_collection = sorted(filtered_collection)
    if len(ordered_collection) >= 2:
        return ordered_collection[1]
    return None