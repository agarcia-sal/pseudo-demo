from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def helper(index_i: int, index_j: int, accum: Set[T]) -> List[T]:
        if index_i > len(list1):
            return sorted(accum)
        if index_j > len(list2):
            return helper(index_i + 1, 1, accum)
        if list1[index_i - 1] != list2[index_j - 1]:
            return helper(index_i, index_j + 1, accum)
        new_accum = accum | {list1[index_i - 1]}
        return helper(index_i, index_j + 1, new_accum)

    return helper(1, 1, set())