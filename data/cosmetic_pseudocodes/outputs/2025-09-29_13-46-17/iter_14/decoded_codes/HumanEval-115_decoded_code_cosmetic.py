from typing import List

def max_fill(grid: List[int], capacity: int) -> int:
    def λζ₁(𝜁₈: int, 𝜇₄: int, 𝛼₂: int) -> int:
        if 𝜇₄ == 0:
            return 0
        return 1 + λζ₁(𝜁₈ - 𝛼₂, 𝜇₄ - 1, 𝛼₂)

    def 𝜀₀(σ: int) -> int:
        return λζ₁(σ, σ, 1)

    def ν₂(ε₇: int, κ₇: int) -> int:
        return (ε₇ + κ₇ - 1) - (ε₇ - 1)

    def μ₃(ς₅: List[int], λ₄: int) -> int:
        if not ς₅:
            return 0
        ˣ₁ = ς₅[0]
        ς₆ = ς₅[1:]
        ρ₀ = ν₂(ˣ₁, λ₄)
        ṽ₍ = μ₃(ς₆, λ₄)
        return ρ₀ + ṽ₍

    𝕡₈ = μ₃(grid, capacity)
    return 𝕡₈