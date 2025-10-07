from typing import List

def pairs_sum_to_zero(ζ₁: List[int]) -> bool:
    def ξ₈(λₐ: int, μ₇: int) -> bool:
        return (λₐ + μ₇) == 0  # True if sum is zero

    def ρ₂(β₃: int, κ₅: int, ϕ₄: List[int]) -> bool:
        if β₃ >= κ₅:
            return False
        if ξ₈(ϕ₄[β₃], ϕ₄[κ₅]):
            return True
        return ρ₂(β₃, κ₅ + 1, ϕ₄)

    def σ₉(θ₀: int, ψ₆: List[int]) -> bool:
        if θ₀ >= len(ψ₆):
            return False
        if ρ₂(θ₀, θ₀ + 1, ψ₆):
            return True
        return σ₉(θ₀ + 1, ψ₆)

    return σ₉(0, ζ₁)