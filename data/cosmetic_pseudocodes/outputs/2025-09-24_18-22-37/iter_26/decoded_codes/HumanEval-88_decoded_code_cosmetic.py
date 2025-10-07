from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)

def sort_array(seq: Sequence[T]) -> List[T]:
    idx_start: int = 0
    sz: int = len(seq)

    if sz == 0:
        return []

    first_elem: T = seq[idx_start]
    last_elem_pos: int = sz - 1
    last_elem: T = seq[last_elem_pos]
    total_val: int = first_elem + last_elem

    remainder: int = total_val % 2
    descending_flag: bool

    if remainder == 0:
        descending_flag = True
    else:
        descending_flag = False

    sorted_result: List[T] = sorted(seq, reverse=descending_flag)
    return sorted_result