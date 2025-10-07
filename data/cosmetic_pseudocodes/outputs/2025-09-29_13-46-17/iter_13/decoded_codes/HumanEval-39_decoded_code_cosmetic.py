from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def Hω⑧ᔷ(ψκ₉: int) -> bool:
            if not (ψκ₉ < 2):
                def πχφƍ(α₇: int) -> bool:
                    # Check if α₇² is not less than ψκ₉ or ψκ₉ == 0
                    if (not ((α₇ * α₇) < ψκ₉)) or (ψκ₉ == 0):
                        return True
                    else:
                        return False

                def ωξμζ(βτ₁: int, γρ₃: int) -> bool:
                    if βτ₁ > γρ₃:
                        return True
                    else:
                        if (ψκ₉ % βτ₁) == 0:
                            return False
                        else:
                            return ωξμζ(βτ₁ + 1, γρ₃)

                limit = min(floor(sqrt(ψκ₉)) + 1, ψκ₉ - 1)
                return ωξμζ(2, limit)
            else:
                return False

        return Hω⑧ᔷ(integer_p)

    def εϵ϶ζ(δσ₄: List[int], ζθ₆: int) -> List[int]:
        if ζθ₆ == 0:
            return δσ₄
        else:
            return εϵ϶ζ([δσ₄[1], δσ₄[0] + δσ₄[1]], ζθ₆ - 1)

    τᚠκᛁ: List[int] = [0, 1]

    def ζλτφ_νρ(κξ₇: List[int], μν₈: int) -> int:
        if μν₈ == 0:
            return τᚠκᛁ[1]
        else:
            ω₃₄₅: List[int] = [κξ₇[1], κξ₇[0] + κξ₇[1]]
            if is_prime(ω₃₄₅[1]):
                return ζλτφ_νρ(ω₃₄₅, μν₈ - 1)
            else:
                return ζλτφ_νρ(ω₃₄₅, μν₈)

    return ζλτφ_νρ(τᚠκᛁ, integer_n)