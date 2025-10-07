from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    outcome = set()
    for idx_a in range(len(list1)):
        for idx_b in range(len(list2)):
            if not (list1[idx_a] != list2[idx_b]):
                outcome.add(list1[idx_a])
    return sorted(outcome)