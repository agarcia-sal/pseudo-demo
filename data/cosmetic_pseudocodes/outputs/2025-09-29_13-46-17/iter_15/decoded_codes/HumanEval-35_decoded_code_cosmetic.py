from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(ξρ: Sequence[T]) -> T:
    def _seek(λψ: T, ϕψ: Sequence[T], κ: int) -> T:
        if κ >= len(ϕψ):
            return λψ
        if ϕψ[κ] > λψ:
            return _seek(ϕψ[κ], ϕψ, κ + 1)
        else:
            return _seek(λψ, ϕψ, κ + 1)
    return _seek(ξρ[0], ξρ, 1)