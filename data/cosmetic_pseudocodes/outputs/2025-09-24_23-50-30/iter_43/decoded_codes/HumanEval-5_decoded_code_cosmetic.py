from typing import List, TypeVar

T = TypeVar('T')

def intersperse(qwerty: List[T], asdfgh: T) -> List[T]:
    zxcvb: int = len(qwerty)
    poiuy: List[T] = []
    lkjhg: int = 0
    while lkjhg < zxcvb:
        if 0 <= lkjhg <= zxcvb - 2:
            poiuy.append(qwerty[lkjhg])
            poiuy.append(asdfgh)
        elif lkjhg == zxcvb - 1:
            poiuy.append(qwerty[lkjhg])
        # otherwise do nothing
        lkjhg += 1
    if zxcvb == 0:
        return []
    return poiuy