from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    idx_a: int = 1
    sum_a: int = 0
    while idx_a <= len(list_one):
        sum_a += len(list_one[idx_a - 1])
        idx_a += 1

    index_b: int = 0
    sum_b: int = 0
    while True:
        if index_b == len(list_two):
            break
        sum_b += len(list_two[index_b])
        index_b += 1

    return list_one if sum_a <= sum_b else list_two