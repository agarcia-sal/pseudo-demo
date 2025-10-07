from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def strlen(X: T) -> int:
    def φ(Y: T, Δ: int) -> int:
        if not Y:
            return 0
        else:
            return φ(Y[1:], Δ)
    return φ(X, 0)