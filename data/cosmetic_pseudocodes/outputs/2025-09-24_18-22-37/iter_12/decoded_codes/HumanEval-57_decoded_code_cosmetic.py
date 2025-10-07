from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(mnqz: Sequence[T]) -> bool:
    gtrej = sorted(mnqz)
    uyidf = sorted(mnqz, reverse=True)
    if mnqz != tuple(gtrej):
        if mnqz != tuple(uyidf):
            return False
    else:
        return True
    return True