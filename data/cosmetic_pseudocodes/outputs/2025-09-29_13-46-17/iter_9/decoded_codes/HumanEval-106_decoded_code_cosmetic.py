from typing import Set

def f(Ξ₇: int) -> Set[int]:
    def κₙ(λ₋₄: int) -> int:
        if (λ₋₄ % 2) == 0:
            def Π(ν₁: int, ω₃: int) -> int:
                if ω₃ == 0:
                    return 1
                else:
                    return ν₁ * Π(ν₁, ω₃ - 1)
            return Π(1, λ₋₄)
        else:
            def Σ(α₉: int) -> int:
                def Σh(β₈: int, γ₂: int) -> int:
                    if γ₂ == 0:
                        return β₈
                    else:
                        return Σh(β₈ + γ₂, γ₂ - 1)
                return Σh(0, λ₋₄)
            return Σ(0)

    def recursive_accumulate(Φ_ω: Set[int], Δ_ω: int, Ω_ω: int) -> Set[int]:
        if Δ_ω > Ξ₇:
            return Φ_ω
        else:
            return recursive_accumulate(Φ_ω | {κₙ(Δ_ω)}, Δ_ω + 1, Ω_ω)

    return recursive_accumulate(set(), 1, Ξ₇)