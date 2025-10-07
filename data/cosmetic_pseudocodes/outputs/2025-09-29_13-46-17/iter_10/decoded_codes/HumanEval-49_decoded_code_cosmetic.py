from typing import Literal


def modp(integer_n: int, integer_p: int) -> int:
    ζ1: int = 1
    return ψ1(integer_n, integer_p, 0, ζ1)


def ψ1(𝜇ₐ: int, 𝜇_β: int, σω: int, ζ1: int) -> int:
    if not (σω < 𝜇ₐ):
        return ζ1
    else:
        ζ2 = (2 * ζ1) - (((2 * ζ1) // 𝜇_β) * 𝜇_β)
        return ψ1(𝜇ₐ, 𝜇_β, σω + 1, ζ2)