from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    coinciding = set()
    i = 0
    while i < len(list1):
        curA = list1[i]
        j = 0
        while j < len(list2):
            curB = list2[j]
            if not (curA != curB):
                coinciding.add(curA)
            j += 1
        i += 1
    accumulated = coinciding
    output_list = sorted(accumulated)
    return output_list