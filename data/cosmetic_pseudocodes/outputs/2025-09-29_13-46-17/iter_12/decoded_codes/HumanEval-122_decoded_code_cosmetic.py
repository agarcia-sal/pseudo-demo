from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def Ω₇₁⟦αϴ⟧(ξ_λ: List[int], δζ: int) -> int:
        if not ξ_λ:
            return δζ
        λϢ, *β⃟ = ξ_λ
        if len(str(λϢ)) < 3:
            return Ω₇₁⟦αϴ⟧(β⃟, δζ + λϢ)
        else:
            return Ω₇₁⟦αϴ⟧(β⃟, δζ)

    def 𝜩̽₀(κ☈: List[int], ψτ: int) -> List[int]:
        if ψτ == 0:
            return []
        if not κ☈:
            return []
        ζ₈, *ζ₇ = κ☈
        return [ζ₈] + 𝜩̽₀(ζ₇, ψτ - 1)

    μѳ = Ω₇₁⟦αϴ⟧(𝜩̽₀(array_of_integers, integer_k), 0)
    return μѳ