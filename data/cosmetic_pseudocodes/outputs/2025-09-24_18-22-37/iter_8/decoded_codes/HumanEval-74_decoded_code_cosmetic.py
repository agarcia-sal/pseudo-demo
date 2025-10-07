from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(array_a: Sequence[T], array_b: Sequence[T]) -> Sequence[T]:
    count_a: int = 0
    idx_a: int = 0
    while idx_a < len(array_a):
        curr_elem_a: T = array_a[idx_a]
        len_curr_elem_a: int = len(curr_elem_a)
        count_a += len_curr_elem_a
        idx_a += 1

    count_b: int = 0
    position_b: int = 0
    while position_b < len(array_b):
        element_b: T = array_b[position_b]
        size_element_b: int = len(element_b)
        count_b += size_element_b
        position_b += 1

    if count_a > count_b:
        return array_b
    else:
        return array_a