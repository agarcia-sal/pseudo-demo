from typing import Sequence, TypeVar, List

T = TypeVar('T')

def common(collectionA: Sequence[T], collectionB: Sequence[T]) -> List[T]:
    acc_set: set[T] = set()
    index_outer: int = 0
    index_inner: int = 0

    while index_outer < len(collectionA):
        curr_outer = collectionA[index_outer]
        match_found = False

        while index_inner < len(collectionB):
            curr_inner = collectionB[index_inner]
            if curr_outer == curr_inner:
                match_found = True

            if match_found:
                acc_set.add(curr_outer)
                index_inner = len(collectionB)  # exit inner loop
            else:
                index_inner += 1

        index_outer += 1
        index_inner = 0

    result_list: List[T] = [elem for elem in acc_set]
    return sorted(result_list)