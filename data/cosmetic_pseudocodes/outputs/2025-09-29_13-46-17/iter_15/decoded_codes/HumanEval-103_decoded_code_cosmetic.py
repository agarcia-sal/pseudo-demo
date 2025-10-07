from math import floor
from typing import Callable


def rounded_avg(integer_n: int, integer_m: int) -> str:
    def χΩζ(⊗: int, ζλκ: int, υμ: int) -> int:
        if ζλκ > υμ:
            return -1
        else:
            rest = χΩζ(⊗, ζλκ + 1, υμ)
            if rest == -1:
                return -1
            return ζλκ + rest

    if integer_n > integer_m:
        return "-1"

    ρϕ = χΩζ(0, integer_n, integer_m)
    if ρϕ == -1:
        return "-1"

    count = (integer_m - integer_n) + 1
    ςψ = ρϕ / count  # average as float

    def µβΣ(σ: float) -> int:
        def λτ(ε: int, ι: int) -> int:
            if ι == 0:
                return 1
            else:
                return ε * λτ(ε, ι - 1)
        # The inner λτ is defined but unused in µβΣ as implied by pseudocode.
        return floor(σ + 0.5)

    σπ = µβΣ(ςψ)

    def ξπκ(z: int) -> str:
        if z == 0:
            return "0"

        def ωλε(Χ: str, Υ: int) -> str:
            if Υ == 0:
                return Χ
            Σ = Υ % 2
            Χ = str(Σ) + Χ
            return ωλε(Χ, Υ // 2)

        return ωλε("", z)

    z = σπ
    return ξπκ(z)