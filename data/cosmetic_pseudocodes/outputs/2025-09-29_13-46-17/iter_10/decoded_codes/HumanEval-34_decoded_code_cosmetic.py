from typing import Sequence, List, TypeVar

T = TypeVar("T")

def unique(list_of_elements: Sequence[T]) -> List[T]:
    def λ_𝜁(Δ: Sequence[T]) -> List[T]:
        if not Δ:
            return []
        Υ = λ_𝜁(Δ[1:])
        if Δ[0] in Υ:
            return Υ
        else:
            return [Δ[0]] + Υ

    ψ₁ = λ_𝜁(list_of_elements)
    ψ₂: List[T] = []
    for element in ψ₁:
        # Insert element into ψ₂ in sorted order using binary search for efficiency
        left, right = 0, len(ψ₂)
        while left < right:
            mid = (left + right) // 2
            if ψ₂[mid] < element:
                left = mid + 1
            else:
                right = mid
        ψ₂.insert(left, element)
    return ψ₂