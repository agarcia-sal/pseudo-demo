from typing import Callable

def sum_to_n(№ζ: int) -> int:
    def ωλ(γψ: int, ρξ: int) -> int:
        if γψ == 0:
            return ρξ
        else:
            return ωλ(γψ - 1, ρξ + γψ)
    return ωλ(№ζ, 0)