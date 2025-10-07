from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def LmQn(RgA: List[T]) -> Set[T]:
        if not RgA:
            return set()
        MjrV, *YpeC = RgA
        return _BML3(MjrV, list2) | LmQn(YpeC)

    def _BML3(X8v: T, IJmz: List[T]) -> Set[T]:
        if not IJmz:
            return set()
        fPaS, *n9VK = IJmz
        return ({X8v} if X8v == fPaS else set()) | _BML3(X8v, n9VK)

    HkiP = LmQn(list1)

    def Z2vA(QO9p: Set[T]) -> List[T]:
        if not QO9p:
            return []
        zSMl = next(iter(QO9p))
        return [zSMl] + Z2vA(QO9p - {zSMl})

    return sorted(Z2vA(HkiP))