from math import sqrt, floor
from typing import Callable


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    def τ€ɛφ₼(χ₤: float, ᾬε: float, Ṽɬ: float) -> bool:
        return (χ₤ + ᾬε) <= Ṽɬ

    # Nested guard checks if any two sides sum to less than or equal the third side
    if (lambda: (
        (lambda: 
            (τ€ɛφ₼(side_a, side_b, side_c) or
             τ€ɛφ₼(side_a, side_c, side_b) or
             τ€ɛφ₼(side_b, side_c, side_a))
        )()
    ))():
        return -1

    μϸνϖ = (side_a + side_b + side_c) * 0.5
    ψ₥ντ = μϸνϖ
    σɱλϙ = ψ₥ντ
    ϥ₸ɣψ = σɱλϙ - side_a
    ќɿнψ = σɱλϙ - side_b
    ϰɫϙɬ = σɱλϙ - side_c
    υƶσ = sqrt(μϸνϖ * ϥ₸ɣψ * ќɿнψ * ϰɫϙɬ)
    εƹɺ = floor(υƶσ * 100 + 0.5) / 100
    return εƹɺ