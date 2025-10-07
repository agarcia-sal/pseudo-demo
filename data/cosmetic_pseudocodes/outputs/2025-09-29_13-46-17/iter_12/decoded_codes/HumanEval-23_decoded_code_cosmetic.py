from typing import Sequence, TypeVar

T = TypeVar('T')

def strlen(𝛙: Sequence[T]) -> int:
    λ: int = 0

    def Ω(ξ: Sequence[T], ς: int) -> int:
        if not ξ:
            return ς
        else:
            return Ω(ξ[1:], ς + 1)

    return λ + Ω(𝛙, 0)