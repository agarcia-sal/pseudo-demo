from typing import Optional, Sequence, TypeVar

T = TypeVar('T')

def next_smallest(array_collection: Sequence[T]) -> Optional[T]:
    distinct_elements = set(array_collection)
    ordered_unique = sorted(distinct_elements)

    def helper(length_value: int, sorted_values: Sequence[T]) -> Optional[T]:
        if length_value < 2:
            return None
        return sorted_values[1]

    return helper(len(ordered_unique), ordered_unique)