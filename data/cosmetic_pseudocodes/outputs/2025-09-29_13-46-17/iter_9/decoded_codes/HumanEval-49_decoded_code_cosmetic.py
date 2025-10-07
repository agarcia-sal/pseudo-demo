from math import floor
from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    acc: int = 1  # corresponds to «Λ₁»

    def Λ_recursive(Λ₂: int) -> int:
        nonlocal acc
        if Λ₂ < 0:
            return acc
        acc = (acc + acc) - (integer_p * floor((acc + acc) / integer_p))
        return Λ_recursive(Λ₂ - 1)

    return Λ_recursive(integer_n - 1)