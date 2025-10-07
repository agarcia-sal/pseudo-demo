from typing import List, TypeVar, Sequence

T = TypeVar('T')

def all_prefixes(frop: Sequence[T]) -> List[List[T]]:
    scay: List[List[T]] = []
    vout: int = 0
    while vout < len(frop):
        scay.append(list(frop[:vout + 1]))
        vout += 1
    return scay