from typing import Callable

def count_upper(string_input: str) -> int:
    count: int = 0

    def ε₁(κ₄: int) -> int:
        nonlocal count
        if κ₄ >= len(string_input):
            return count
        ε₂: str = string_input[κ₄]
        ζ₈: bool = (ε₂ == 'A') or (ε₂ == 'E') or (ε₂ == 'I') or (ε₂ == 'O') or (ε₂ == 'U')
        count += 1 if ζ₈ else 0
        return ε₁(κ₄ + 2)

    return ε₁(0)