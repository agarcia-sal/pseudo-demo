from typing import Callable

def sum_to_n(integer_n: int) -> int:
    ζₗₓ₈: int = 0
    Ϟₘ₉ɸ: int = 0

    def ψ₭ₒₚ(ωₖₐ: int) -> int:
        if ωₖₐ < 0:
            return 0
        else:
            return ωₖₐ + ψ₭ₒₚ(ωₖₐ - 1)

    ζₗₓ₈ = ψ₭ₒₚ(integer_n)
    return ζₗₓ₈