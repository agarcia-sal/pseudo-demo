from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    acc_length_one: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        curr_element_one: T = list_one[idx_one]
        acc_length_one += len(curr_element_one)
        idx_one += 1

    acc_length_two: int = 0
    idx_two: int = 0
    while idx_two < len(list_two):
        curr_element_two: T = list_two[idx_two]
        acc_length_two += len(curr_element_two)
        idx_two += 1

    if not (acc_length_two < acc_length_one):
        return list_one
    else:
        return list_two