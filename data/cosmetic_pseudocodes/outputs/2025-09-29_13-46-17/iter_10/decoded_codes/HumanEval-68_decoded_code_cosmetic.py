from typing import List, Tuple

def pluck(array_of_nodes: List[int]) -> List[int | int]:
    def τ₉_ξ(θₖ: List[int]) -> List[int | int]:
        if len(θₖ) == 0:
            return []
        ξ₁ = list(filter(lambda σ: σ % 2 == 0, θₖ))
        if len(ξ₁) < 1:
            return []
        μ₀ = min(ξ₁)
        ι = next(idx for idx, val in enumerate(θₖ) if val == μ₀)
        return [μ₀, ι]
    return τ₉_ξ(array_of_nodes)