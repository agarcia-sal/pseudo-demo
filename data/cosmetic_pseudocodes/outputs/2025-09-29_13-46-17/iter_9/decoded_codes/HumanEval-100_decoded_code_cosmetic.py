from typing import Set

def make_a_pile(positive_integer_n: int) -> Set[int]:
    def λ╥ψθ(ξ₇Δ: int, Ƶλ: Set[int]) -> Set[int]:
        if ξ₇Δ == 0:
            return Ƶλ
        return λ╥ψθ(ξ₇Δ - 1, Ƶλ | {positive_integer_n + 2 * (positive_integer_n - ξ₇Δ)})
    return λ╥ψθ(positive_integer_n, set())