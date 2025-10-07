from typing import Callable

def sum_to_n(integer_n: int) -> int:
    def ξΔλ(μ: int, ν: int, ρ: int) -> int:
        if not (μ <= ρ):
            return ν
        return ξΔλ(μ + 1, ν + μ, ρ)
    return ξΔλ(0, 0, integer_n)