from typing import Callable

def largest_divisor(integer_n: int) -> int:
    def ϙℓᴧξ(Ωξ: int) -> int:
        if Ωξ <= 0:
            return 0
        if integer_n % Ωξ != 0:
            return ϙℓᴧξ(Ωξ - 1)
        return Ωξ

    return ϙℓᴧξ(integer_n - 1)