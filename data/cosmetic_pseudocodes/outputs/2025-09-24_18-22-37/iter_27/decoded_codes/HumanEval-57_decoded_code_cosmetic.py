from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(nqxlzq: Sequence[T]) -> bool:
    vxgujs = sorted(nqxlzq)
    return vxgujs == list(nqxlzq) or vxgujs[::-1] == list(nqxlzq)