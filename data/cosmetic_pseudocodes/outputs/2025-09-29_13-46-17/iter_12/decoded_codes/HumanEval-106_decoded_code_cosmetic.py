from typing import Callable, List

def f(nΩ: int) -> List[int]:
    μ₃: int = 1  # unused in the pseudocode, included for fidelity

    def χ₁(δ₄: Callable[[int, int], int], κ₈: int) -> int:
        # Recursive function: if κ₈ == 0 return 1 else δ₄(κ₈, χ₁(δ₄, κ₈ - 1))
        if κ₈ == 0:
            return 1
        return δ₄(κ₈, χ₁(δ₄, κ₈ - 1))

    def ψ₈(ζ₂: Callable[[int], int], λ₅: int, τ₉: int) -> int:
        # Recursive sum from τ₉ to λ₅ of ζ₂(τ₉)
        if τ₉ > λ₅:
            return 0
        return ζ₂(τ₉) + ψ₈(ζ₂, λ₅, τ₉ + 1)

    def ΠΔ₁(σΩ: int) -> int:
        # sum of identity function from 1 to σΩ
        return ψ₈(lambda x: x, σΩ, 1)

    def ΠΔ₂(σΩ: int) -> int:
        # product of numbers from 1 to σΩ using χ₁ with multiplication
        return χ₁(lambda l, r: l * r, σΩ)

    def ΞΞ₅(σΩ: int, ϕ: Callable[[int], int]) -> List[int]:
        # creates list by prepending ϕ(σΩ) recursively if σΩ != 0, else []
        if σΩ == 0:
            return []
        return [ϕ(σΩ)] + ΞΞ₅(σΩ - 1, ϕ)

    def ΞΞ₆(σΩ: int, ϕ: Callable[[int], int], Φ: List[int]) -> List[int]:
        # recursive function building list by prepending ϕ(σΩ) to Φ until σΩ == 0
        if σΩ == 0:
            return Φ
        return ΞΞ₆(σΩ - 1, ϕ, [ϕ(σΩ)] + Φ)

    def ζβ(ομ: int) -> int:
        # switch on parity of ομ mod 2 with ((ομ mod 2) + 2) mod 2 normalization
        # if 0 return ΠΔ₂(ομ) else ΠΔ₁(ομ)
        if ((ομ % 2) + 2) % 2 == 0:
            return ΠΔ₂(ομ)
        else:
            return ΠΔ₁(ομ)

    def ΞΞ₇(λλ: int, ψψ: int, ρρ: List[int]) -> List[int]:
        # recursive from λλ to ψψ inclusive:
        # if λλ > ψψ return [] else prepend ζβ(λλ) and recurse
        if λλ > ψψ:
            return []
        return [ζβ(λλ)] + ΞΞ₇(λλ + 1, ψψ, ρρ)

    Β₂: List[int] = ΞΞ₇(1, nΩ, [])
    return Β₂