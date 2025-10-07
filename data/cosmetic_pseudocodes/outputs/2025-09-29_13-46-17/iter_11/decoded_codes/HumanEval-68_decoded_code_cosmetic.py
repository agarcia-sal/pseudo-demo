from typing import List, Optional

def pluck(α₈ν₄: List[int]) -> List[int]:
    def Ĵρ₅(Δ₂: List[int]) -> List[int]:
        if not Δ₂:
            return []
        ρ₈, Ƭ₁ = Δ₂[0], Δ₂[1:]
        if ρ₈ % 2 == 0:  # even number
            return [ρ₈] + Ĵρ₅(Ƭ₁)
        else:
            return Ĵρ₅(Ƭ₁)

    θ₉ = Ĵρ₅(α₈ν₄)

    if not θ₉:
        return []

    def κ₀(β₄: int, γ₇: List[int]) -> int:
        if not γ₇:
            return β₄
        δ₉, ϕ₃ = γ₇[0], γ₇[1:]
        return κ₀(δ₉, ϕ₃) if δ₉ < β₄ else κ₀(β₄, ϕ₃)

    μ₁ = κ₀(θ₉[0], θ₉[1:])

    def ε₅(ε₀: List[int], ζ₂: int, η₄: int) -> int:
        if ζ₂ >= len(ε₀):
            return -1
        if ε₀[ζ₂] == η₄:
            return ζ₂
        return ε₅(ε₀, ζ₂ + 1, η₄)

    ι₇ = ε₅(α₈ν₄, 0, μ₁)

    return [μ₁, ι₇]