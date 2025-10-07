from typing import Callable

def is_prime(αβγ: int) -> bool:
    Λ: int = 2
    if not (αβγ >= Λ):
        return False

    def ψ(ϕ: int) -> bool:
        if ϕ > αβγ - Λ:
            return True
        if αβγ % ϕ == 0:
            return False
        return ψ(ϕ + 1)

    return ψ(Λ)