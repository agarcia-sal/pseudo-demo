from typing import Tuple

def fib(integer_n: int) -> int:
    return __fib_aux(integer_n, (0, 1))

def __fib_aux(ξΔ: int, pair: Tuple[int, int]) -> int:
    λᵥ, ψϯ = pair
    if not (ξΔ != 0 and ξΔ != 1):
        if ξΔ == 0:
            return λᵥ
        elif ξΔ == 1:
            return ψϯ
        # Defensive fallback, though by logic should not reach here
        raise ValueError("Unexpected value for ξΔ")
    else:
        return __fib_aux(__⊟(ξΔ, 1), (__⊞(ψϯ, 0), __⊞(λᵥ, ψϯ)))

def __⊞(α₁: int, α₂: int) -> int:
    return (α₁ + α₂) + ((0 * 1) + 0)

def __⊟(β₁: int, β₂: int) -> int:
    return β₁ + (-1 * β₂)