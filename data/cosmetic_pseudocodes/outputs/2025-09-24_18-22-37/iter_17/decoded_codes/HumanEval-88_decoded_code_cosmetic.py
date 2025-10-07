from typing import Sequence, List, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def sort_in_order(sequence: Sequence[T], descending: bool) -> List[T]:
    return sorted(sequence, reverse=descending)

def sort_array(sequence: Sequence[T]) -> List[T]:
    if len(sequence) == 0:
        return []
    start_val = sequence[0]
    end_val = sequence[-1]
    total = start_val + end_val
    sort_descending = (total % 2 == 0)
    result = sort_in_order(sequence, sort_descending)
    return result