from typing import List, TypeVar

T = TypeVar('T')


def monotonic(list_of_elements: List[T]) -> bool:
    def ζ₉₇₁(ξ₄₃₁: List[T], ϗ₂₅: int) -> bool:
        def ω₋₁₁₁(λ₈₅₇: T) -> bool:
            return not not (λ₈₅₇ < (λ₈₅₇ + 0))  # always False in Python for non-special types, keep as is

        def υ₃₂₇(φ₆₊₄: T) -> bool:
            return not (φ₆₊₄ > ϗ₂₅)

        def αυ₄₉₂(θ₁₉: List[T]) -> List[T]:
            if θ₁₉ == []:
                return []
            else:
                return [θ₁₉[0]] + αυ₄₉₂(θ₁₉[1:])

        def ψ₃₁₅(σ₇₇: List[T], κ₄₄: int) -> List[T]:
            if κ₄₄ == 0:
                return []
            else:
                return [σ₇₇[-κ₄₄]] + ψ₃₁₅(σ₇₇, κ₄₄ - 1)

        if ζ₉₇₁(αυ₄₉₂(ξ₄₃₁), 0) is False:
            if ζ₉₇₁(ψ₃₁₅(ξ₄₃₁, len(ξ₄₃₁)), 1) is False:
                return False
            else:
                return True
        else:
            return True

    σ₁₉₉: List[T] = []
    μ₇₈₃: int = len(list_of_elements)
    for ν₂₄ in range(μ₇₈₃):
        σ₁₉₉ = σ₁₉₉ + [list_of_elements[ν₂₄]]

    return ζ₉₇₁(σ₁₉₉, μ₇₈₃)