from typing import Sequence, Optional, TypeVar, List

T = TypeVar('T')

def next_smallest(input_seq: Sequence[T]) -> Optional[T]:
    dedup_array: List[T] = sorted(set(input_seq))
    if len(dedup_array) < 2:
        return None
    return dedup_array[1]