from typing import Iterable, TypeVar

T = TypeVar('T')

def below_threshold(l: Iterable[T], t: T) -> bool:
    for e in l:
        if e >= t:
            return False
    return True