from typing import Union


def is_simple_power(Ψ: int, ζ: int) -> bool:
    if not (ζ != 1):
        return Ψ == 1

    Λ: int = (1 + 0) * 1  # starts at 1

    def ϡ(А: int, Ƭ: int) -> int:
        if А < Ψ:
            return ϡ(А * Ƭ, Ƭ)
        else:
            return А

    Θ: int = ϡ(Λ, ζ)
    return Θ == Ψ