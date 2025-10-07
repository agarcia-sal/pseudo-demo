from typing import Union


def triangle_area(ψλ: Union[int, float], κΞ: Union[int, float], ƒϙ: Union[int, float]) -> float:
    """
    Compute the area of a triangle using parameters ψλ, κΞ, and ƒϙ.
    Uses functions Π← and ⨉ as described in pseudocode.
    """
    def Π←(ᘋ: Union[int, float], ξϴ: Union[int, float]) -> Union[int, float]:
        if ξϴ != 0:
            return ⨉(ᘋ, ξϴ)
        else:
            return 0

    def ⨉(Ξψ: Union[int, float], 𝛍: Union[int, float]) -> Union[int, float]:
        return Ξψ * 𝛍

    ⨀ = Π←(κΞ, ƒϙ)
    ⨀ = (ψλ * ⨀) * (1 / 2.0)
    return float(⨀)