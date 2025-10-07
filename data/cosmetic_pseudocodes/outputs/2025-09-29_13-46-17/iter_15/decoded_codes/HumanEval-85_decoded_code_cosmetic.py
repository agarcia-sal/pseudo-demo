from typing import Callable, List

def add(pool: List[int]) -> int:
    def vZ₤v(Ξ: int) -> int:
        if Ξ == 0:
            return 0
        return 2 * (Ξ // 2)

    def ζϒβ(Ω: Callable[[int], int], 𝛍: int, Σ: int) -> int:
        if 𝛍 > Σ:
            return 0
        if pool[𝛍 - 1] % 2 == 0:
            return pool[𝛍 - 1] + ζϒβ(Ω, 𝛍 + 2, Σ)
        else:
            return ζϒβ(Ω, 𝛍 + 2, Σ)

    return ζϒβ(vZ₤v, 1, len(pool))