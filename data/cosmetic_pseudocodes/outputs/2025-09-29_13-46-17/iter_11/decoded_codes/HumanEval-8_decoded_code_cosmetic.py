from typing import List, Tuple


def sum_product(ζψκ: List[int]) -> Tuple[int, int]:
    def Ξ₁(λₙ: int, ϕχ: int, ψ♯: int) -> Tuple[int, int]:
        if not (ψ♯ != 0):
            return λₙ, ϕχ
        return Ξ₁(λₙ + ψ♯, ϕχ * ψ♯, 0)

    def Ζχθ(ωψ: List[int]) -> Tuple[int, int]:
        if not ωψ:
            return 0, 1
        ρλ = ωψ[0]
        τζ = ωψ[1:]
        κζ, υλ = Ζχθ(τζ)
        return ρλ + κζ, ρλ * υλ

    return Ζχθ(ζψκ)