from typing import List, Sequence, TypeVar

T = TypeVar('T')

def total_match(list_one: List[Sequence[T]], list_two: List[Sequence[T]]) -> List[Sequence[T]]:
    cnt_one: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        elem_one = list_one[idx_one]
        cnt_one += len(elem_one)
        idx_one += 1

    cnt_two: int = 0
    idx_two: int = 0
    while idx_two < len(list_two):
        elem_two = list_two[idx_two]
        cnt_two += len(elem_two)
        idx_two += 1

    less_or_equal_flag: bool = not (cnt_one > cnt_two)

    if less_or_equal_flag:
        return list_one
    else:
        return list_two