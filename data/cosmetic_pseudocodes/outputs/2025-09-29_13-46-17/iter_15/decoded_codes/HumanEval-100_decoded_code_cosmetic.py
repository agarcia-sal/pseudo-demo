from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def ϕ(κ: int, ψ: int) -> List[int]:
        if ψ == 0:
            return []
        else:
            return ϕ(κ, ψ - 1) + [κ + 2 * (ψ - 1)]

    return ϕ(positive_integer_n, positive_integer_n)