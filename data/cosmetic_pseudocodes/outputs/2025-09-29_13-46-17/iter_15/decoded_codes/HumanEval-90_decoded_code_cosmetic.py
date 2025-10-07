from typing import List, Set, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    def ψ₃(α₁: List[int], β₅: Set[int]) -> Set[int]:
        if not α₁:
            return β₅
        χ₇, *rest = α₁
        if χ₇ in β₅:
            return ψ₃(rest, β₅)
        return ψ₃(rest, β₅ | {χ₇})

    ξ₂: Set[int] = ψ₃(list_of_integers, set())

    def λ₄(μ₈: Set[int]) -> List[int]:
        if not μ₈:
            return []
        ν₁ = next(iter(μ₈))
        ο₆ = λ₄(μ₈ - {ν₁})

        def σ₀(τ₃: int, υ₂: List[int]) -> List[int]:
            if not υ₂:
                return [τ₃]
            π₇, *rest = υ₂
            if τ₃ < π₇:
                return [τ₃] + υ₂
            return [π₇] + σ₀(τ₃, rest)

        return σ₀(ν₁, ο₆)

    ζ₅: List[int] = λ₄(ξ₂)
    if len(ζ₅) < 2:
        return None
    return ζ₅[1]