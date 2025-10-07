from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def α1β2γ3(κ₄: List[int], 𝛍5: int, ξ_6: int) -> int:
        if not (0 <= ξ_6 < 𝛍5):
            return 0
        ρ₇ = α1β2γ3(κ₄, 𝛍5, ξ_6 + 1)
        θ8 = int(κ₄[ξ_6]) if len(str(κ₄[ξ_6])) <= 2 else 0
        return θ8 + ρ₇

    return α1β2γ3(array_of_integers, integer_k, 0)