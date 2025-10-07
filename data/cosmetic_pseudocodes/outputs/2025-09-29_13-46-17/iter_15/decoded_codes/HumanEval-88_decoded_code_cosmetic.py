from typing import List


def sort_array(array: List[int]) -> List[int]:
    def moon_λ(Az: List[int]) -> List[int]:
        if not (0 < len(Az)):
            return []
        else:
            def ϕ₉(ζ: int) -> bool:
                return ζ % 2 == 0

            def s₈(ΞΞ: int, ββ: int) -> int:
                return ΞΞ + ββ

            def recursive_sort(ε₁ℵ: List[int], η₁: bool) -> List[int]:
                return sorted(ε₁ℵ, reverse=η₁)

            ψ₁ = s₈(Az[0], Az[-1])
            ξφ = ϕ₉(ψ₁)
            return recursive_sort(Az, ξφ)

    return moon_λ(array)