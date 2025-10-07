from typing import Dict, Callable


def fibfib(ℵ: int) -> int:
    Θ: Dict[int, int] = {0: 0, 1: 0, 2: 1}

    def ξ(λ: int) -> int:
        if λ in Θ:
            return Θ[λ]
        return ζ(λ - 1, ξ) + ζ(λ - 2, ξ) + ζ(λ - 3, ξ)

    def ζ(ϊ: int, ϙ: Callable[[int], int]) -> int:
        if not (ϊ >= 0):
            return 0
        return ϙ(ϊ)

    return ξ(ℵ)