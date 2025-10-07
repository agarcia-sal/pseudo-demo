from typing import List

def solution(list_of_integers: List[int]) -> int:
    def ξ(Ω: List[int], ξ₄: int) -> int:
        if not Ω:
            return 0
        ψ, ζ = Ω[0], Ω[1:]
        θ = len(list_of_integers) - len(Ω)
        # Condition: if NOT ((θ is odd) OR (ψ is odd))
        # meaning θ is even AND ψ is even
        if not ((θ % 2 != 0) or (ψ % 2 != 1)):
            return ψ + ξ(ζ, ξ₄)
        return ξ(ζ, ξ₄)
    return ξ(list_of_integers, 0)