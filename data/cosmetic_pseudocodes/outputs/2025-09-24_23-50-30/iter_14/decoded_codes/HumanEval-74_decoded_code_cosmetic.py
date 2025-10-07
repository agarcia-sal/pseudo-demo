from typing import List, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    acc_one: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        acc_one += len(list_one[idx_one])
        idx_one += 1

    acc_two: int = 0
    idx_two: int = 0
    while idx_two < len(list_two):
        acc_two += len(list_two[idx_two])
        idx_two += 1

    if not (acc_one > acc_two):
        return list_one
    return list_two