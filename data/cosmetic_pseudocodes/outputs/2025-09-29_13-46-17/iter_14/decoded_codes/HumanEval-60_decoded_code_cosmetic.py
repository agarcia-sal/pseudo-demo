from typing import Callable

def sum_to_n(integer_n: int) -> int:
    def λₐ(ζ: int, ρ: int) -> int:
        if ζ > ρ:
            return 0
        return ζ + λₐ(ζ + 1, ρ)
    return λₐ(0, integer_n)