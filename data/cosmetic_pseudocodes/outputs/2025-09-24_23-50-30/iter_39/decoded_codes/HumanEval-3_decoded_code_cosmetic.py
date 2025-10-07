from typing import List


def below_zero(alist: List[int]) -> bool:
    acc: int = 0
    idx: int = 0
    while idx < len(alist):
        acc += alist[idx]
        if acc < 0:
            return True
        idx += 1
    return False