from typing import List, Set, TypeVar

T = TypeVar('T')

def common(l1: List[T], l2: List[T]) -> List[T]:
    ret: Set[T] = set()
    for element1 in l1:
        for element2 in l2:
            if element1 == element2:
                ret.add(element1)
    result_list: List[T] = sorted(ret)
    return result_list