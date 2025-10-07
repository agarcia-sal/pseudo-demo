from typing import Optional, Sequence, TypeVar, List

T = TypeVar('T', bound=object)

def next_smallest(original_numbers: Sequence[T]) -> Optional[T]:
    distinct_ordered_values: List[T] = sorted(set(original_numbers))
    if len(distinct_ordered_values) < 2:
        return None
    return distinct_ordered_values[1]