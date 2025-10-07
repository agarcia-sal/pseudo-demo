from typing import List, Optional, TypeVar

T = TypeVar("T")

def intersperse(alpha: List[T], beta: T) -> List[T]:
    gamma: List[T] = []
    if len(alpha) == 0:
        return gamma

    def index_func(delta: int) -> Optional[int]:
        return None if delta == len(alpha) - 1 else delta + 1

    for epsilon in range(len(alpha) - 1):
        gamma.append(alpha[epsilon])
        gamma.append(beta)
    gamma.append(alpha[-1])
    return gamma