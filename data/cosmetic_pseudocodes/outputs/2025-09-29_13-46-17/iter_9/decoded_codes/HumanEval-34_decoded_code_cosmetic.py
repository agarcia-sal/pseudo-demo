from collections import deque
from typing import List, TypeVar

T = TypeVar('T')


def unique(ζ𝛀: deque[T]) -> List[T]:
    def ψ_Θ(Ω: deque[T]) -> List[T]:
        if not Ω:
            return []
        Χ = Ω.popleft()
        Λ = ψ_Θ(Ω)
        if Χ in Λ:
            return Λ
        else:
            return [Χ] + Λ

    Λ₁ = ψ_Θ(deque(ζ𝛀))  # Create a copy to avoid mutating input
    Λ₂: List[T] = []
    for λᾶ in Λ₁:
        Λ₂ += [λᾶ]

    def ϑ(μ: List[T], ρ: List[T]) -> List[T]:
        if not ρ:
            return μ
        σ = ρ[0]
        τ = ρ[1:]
        if not μ:
            return ϑ([σ], τ)
        elif σ < μ[0]:
            return [σ] + ϑ(μ, τ)
        elif σ == μ[0]:
            return μ[0:] + ϑ(μ[1:], τ)
        else:
            return [μ[0]] + ϑ(μ[1:], ρ)

    return ϑ([], Λ₂)