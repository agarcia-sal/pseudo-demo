from typing import List, Set, TypeVar

T = TypeVar('T', bound=object)  # General element type


def common(arrA: List[T], arrB: List[T]) -> List[T]:
    def nestRec(ix: int, jx: int, coll: Set[T]) -> Set[T]:
        if ix >= len(arrA):
            return coll
        if jx >= len(arrB):
            return nestRec(ix + 1, 0, coll)
        if arrA[ix] != arrB[jx]:
            return nestRec(ix, jx + 1, coll)
        else:
            return nestRec(ix, jx + 1, coll.union({arrA[ix]}))

    collected = nestRec(0, 0, set())
    return sorted(collected)