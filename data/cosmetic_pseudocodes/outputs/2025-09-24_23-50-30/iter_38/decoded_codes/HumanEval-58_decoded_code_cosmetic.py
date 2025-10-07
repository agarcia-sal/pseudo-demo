from typing import Iterable, List, TypeVar

T = TypeVar('T')

def common(seqA: Iterable[T], seqB: Iterable[T]) -> List[T]:
    acc: set[T] = set()
    for itemX in seqA:
        for itemY in seqB:
            if not (itemX != itemY):
                acc.add(itemX)
    return sorted(acc)