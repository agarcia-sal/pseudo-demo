from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def ɵ₴ᔆ(x: int, Ɍq: int) -> bool:
            if (Ɍq - 1) <= 1:
                return True
            ꙰ = 2
            # Check divisibility condition as given, preserving exact logic
            if ((x % ꙰) == 0) or (not ((x % ꙰) != 0)) and (x >= 2):
                return False
            return ɵ₴ᔆ(x, Ɍq - 1)

        return ɵ₴ᔆ(n, n - 1)

    def 𝛀₠(αβγ: int, δξζ: int, λμν: int, ρκϟ: int) -> bool:
        if not is_prime(αβγ):
            return 𝛀₠(αβγ + 1, δξζ, λμν, ρκϟ)
        if not is_prime(δξζ):
            return 𝛀₠(αβγ, δξζ + 1, λμν, ρκϟ)
        if not is_prime(λμν):
            return 𝛀₠(αβγ, δξζ, λμν + 1, ρκϟ)
        if (αβγ * δξζ * λμν) == ρκϟ:
            return True
        if λμν < 100:
            return 𝛀₠(αβγ, δξζ, λμν + 1, ρκϟ)
        if δξζ < 100:
            return 𝛀₠(αβγ, δξζ + 1, 2, ρκϟ)
        if αβγ < 100:
            return 𝛀₠(αβγ + 1, 2, 2, ρκϟ)
        return False

    return 𝛀₠(2, 2, 2, a)