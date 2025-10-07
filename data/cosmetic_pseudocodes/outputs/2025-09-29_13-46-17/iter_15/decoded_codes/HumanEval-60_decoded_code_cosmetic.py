from typing import Callable

def sum_to_n(integer_n: int) -> int:
    def δ₇𝜓(ξ₉: int, Ϯ₄: int) -> int:
        if ξ₉ > Ϯ₄:
            return 0
        else:
            return ξ₉ + δ₇𝜓(ξ₉ + 1, Ϯ₄)
    return δ₇𝜓(0, integer_n)