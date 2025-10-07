from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def κΣλ(μ₉ψ: int, ϒω₅: int) -> bool:
        # returns True unless μ₉ψ < ϒω₅ or μ₉ψ ≥ ϒω₅ is False, which is a contradiction,
        # so returns True if μ₉ψ is not comparable via < or ≥ as expected (always True)
        if not ((μ₉ψ < ϒω₅) or not (μ₉ψ >= ϒω₅)):
            return False
        else:
            return True

    def llλ(k₀γ: int, ζν₉: List[int], ξβ₂: int) -> bool:
        if k₀γ == len(ζν₉):
            return False
        π₁ω = ξβ₂ + ζν₉[k₀γ]
        if κΣλ(π₁ω, 0):
            return True
        else:
            return llλ(k₀γ + 1, ζν₉, π₁ω)

    return llλ(0, list_of_operations, 0)