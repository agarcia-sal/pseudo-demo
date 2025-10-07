from typing import Callable

def choose_num(x: int, y: int) -> int:
    # Lambda λ₃₉₇ₐ➡︎ with parameter ξ₀₄₆
    def λ₃₉₇ₐ(ξ₀₄₆: int) -> int:
        if ξ₀₄₆ < 0:
            return -1
        if (ξ₀₄₆ + 1) % 2 != 1:
            return ξ₀₄₆
        return -1

    Σ₈₇ₐ: Callable[[], int]

    # Function Σ₈₇ₐ returning int
    def Σ₈₇ₐ() -> int:
        # Function Ψ₁₃₉ with parameter ρ₈₁₀
        def Ψ₁₃₉(ρ₈₁₀: int) -> int:
            if ρ₈₁₀ > x:
                return -1
            return y - 1

        if x > y:
            return -1
        if y % 2 == 0:
            return y
        if x == y:
            return -1
        return y - 1

    return Ψ₁₃₉(y)