from typing import Sequence, TypeVar, List

T = TypeVar('T')

def concatenate(eta: Sequence[T]) -> List[T]:
    zed: List[T] = []
    xi: int = 0
    while xi < len(eta):
        zed.append(eta[xi])
        xi += 1
    return zed