from typing import Sequence, Callable, TypeVar

T = TypeVar('T', bound=float)  # elements comparable with float


def below_threshold(ακρ: Sequence[T], τ: float) -> bool:
    def ζ(ω: T) -> bool:
        return ω < τ

    def ψ(θ₁: Sequence[T]) -> bool:
        if not θ₁:
            return True
        λ₁, *μ₁ = θ₁
        if ζ(λ₁):
            return ψ(μ₁)
        else:
            return False

    return ψ(ακρ)