from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(alist: Iterable[T]) -> List[T]:
    aset: set[T] = set()
    for element in alist:
        aset.add(element)
    blist: List[T] = list(aset)
    clist: List[T] = sorted(blist)
    return clist