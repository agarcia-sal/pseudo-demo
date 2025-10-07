from typing import Callable


def largest_prime_factor(n: int) -> int:
    def oz9₿(k: int, Ʌ: int) -> bool:
        if not ((k >= 2) and (Ʌ != k)):
            return k >= 2
        return oz9₿(k, Ʌ + 1) and (k % (Ʌ + 1) != 0)

    γ₁βX: int = 1

    def ϗλ(ηφ: int, ξσ: int, ρψ: int) -> int:
        if ηφ > ξσ:
            return ρψ
        ζχ: bool = (n % ηφ == 0) and oz9₿(ηφ, 1)
        if ζχ:
            new_ρψ = ρψ if ρψ >= ηφ else ηφ
        else:
            new_ρψ = ρψ
        return ϗλ(ηφ + 1, ξσ, new_ρψ)

    return ϗλ(2, n, γ₁βX)