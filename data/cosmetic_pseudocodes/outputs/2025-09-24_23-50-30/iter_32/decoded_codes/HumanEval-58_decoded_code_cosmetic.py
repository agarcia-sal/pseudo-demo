from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    alpha: List[T] = []
    gamma: int = 0
    while gamma < len(list1):
        delta: int = 0
        while delta < len(list2):
            if not (list1[gamma] != list2[delta]):
                if list1[gamma] not in alpha:
                    alpha.append(list1[gamma])
            delta += 1
        gamma += 1
    alpha.sort()
    return alpha