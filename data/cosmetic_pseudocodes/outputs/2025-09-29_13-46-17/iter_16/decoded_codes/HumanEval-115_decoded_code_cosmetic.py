from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def φξ₋λ(μς: List[int], ῶζ: int, κπ: int, χₜ: int) -> int:
        if χₜ <= 0:
            return 0
        # Recursive choice: if sum including μς[κπ] plus recursive call > χₜ, return χₜ,
        # else return 1 + recursive call with restarting ῶζ as 0 and next index
        if ῶζ + φξ₋λ(μς, ῶζ + μς[κπ], κπ + 1, χₜ - 1) > χₜ:
            return χₜ
        else:
            return 1 + φξ₋λ(μς, 0, κπ + 1, χₜ)

    def ɣµν(εψ: List[int], ιε: int) -> int:
        if ιε == len(εψ):
            return 0
        return εψ[ιε] + ɣµν(εψ, ιε + 1)

    def τζ(βυξ: List[List[int]], Ϙθ: int, ιε: int, ςρ: int) -> int:
        if ιε == len(βυξ):
            return ςρ
        υλ = ROUND_UP(ɣµν(βυξ[ιε], 0) / Ϙθ)
        return τζ(βυξ, Ϙθ, ιε + 1, ςρ + υλ)

    def ROUND_UP(ζ: float) -> int:
        from math import floor
        f = floor(ζ)
        return f + 1 if ζ - f > 0 else f

    return τζ(grid, capacity, 0, 0)