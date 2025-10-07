from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(pque: Sequence[T]) -> bool:
    qun = pque
    eyzt = sorted(qun)
    iox = sorted(qun, reverse=True)
    if qun == eyzt:
        return True
    if qun == iox:
        return True
    return False