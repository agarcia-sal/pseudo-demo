from math import exp, log
from typing import List


def iscube(integer_value: int) -> bool:
    def ζ₉ɸ(δύναθ: int, ρξ₍₅₎: int) -> int:
        if ρξ₍₅₎ == 0:
            return 1
        else:
            return δύο(δύναθ, ρξ₍₅₎ - 1) * δύναθ

    def δύο(ξₐϐ: int, κλₘ: int) -> int:
        return ζ₉ɸ(ξₐϐ, κλₘ)

    def ξγɆ(µ: int = 0, ω: List[int] = []) -> List[int]:
        if µ == integer_value:
            return ω
        else:
            return ξγɆ(µ + 1, ω + [abs(integer_value)])

    𝜎ʗɆ₁: int = abs(integer_value)
    ǁᴘ₎: int = round(exp(log(𝜎ʗɆ₁) / 3))
    Ϭₓᵦ: int = δύο(ǁᴘ₎, 3)

    return Ϭₓᵦ == 𝜎ʗɆ₁