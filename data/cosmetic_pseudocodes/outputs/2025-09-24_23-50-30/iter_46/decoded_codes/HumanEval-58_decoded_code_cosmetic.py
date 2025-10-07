from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def aux_outer(index1: int, accum: Set[T]) -> Set[T]:
        if index1 >= len(list1):
            return accum

        def aux_inner(index2: int, inner_accum: Set[T]) -> Set[T]:
            if index2 >= len(list2):
                return inner_accum
            if not (list1[index1] != list2[index2]):  # equivalent to list1[index1] == list2[index2]
                return aux_inner(index2 + 1, inner_accum | {list1[index1]})
            else:
                return aux_inner(index2 + 1, inner_accum)

        return aux_outer(index1 + 1, aux_inner(0, accum))

    return sorted(list(aux_outer(0, set())))