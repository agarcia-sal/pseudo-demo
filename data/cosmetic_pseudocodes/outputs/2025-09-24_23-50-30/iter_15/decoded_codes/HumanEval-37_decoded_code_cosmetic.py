from collections import deque
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_even(input_seq: Sequence[T]) -> List[T]:
    alt_elems_one: deque[T] = deque()
    alt_elems_two: deque[T] = deque()

    idx_num: int = 0
    length: int = len(input_seq)
    while idx_num < length:
        if idx_num % 2 == 0:
            alt_elems_one.append(input_seq[idx_num])
        else:
            alt_elems_two.append(input_seq[idx_num])
        idx_num += 1

    sorted_elems_one: List[T] = []
    while alt_elems_one:
        sorted_elems_one.append(alt_elems_one.popleft())
    sorted_elems_one.sort()

    sorted_elems_two: List[T] = []
    while alt_elems_two:
        sorted_elems_two.append(alt_elems_two.popleft())

    result_sequence: List[T] = []
    pos: int = 0
    limit: int = len(sorted_elems_two)
    while pos < limit:
        result_sequence.append(sorted_elems_one[pos])
        result_sequence.append(sorted_elems_two[pos])
        pos += 1

    if len(sorted_elems_two) < len(sorted_elems_one):
        result_sequence.append(sorted_elems_one[-1])

    return result_sequence