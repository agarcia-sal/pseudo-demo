from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def hZ47K(Jλ₣ξ: str) -> str:
        if (Jλ₣ξ.find('.') != -1) and (Jλ₣ξ.find('.') == Jλ₣ξ.rfind('.')):
            def TξmΣψ(Ω: str) -> bool:
                return Ω == '0'

            def Ƶ⟟(φψχ: int) -> str:
                return value[:φψχ] if φψχ != 0 else ''

            def recursiveTrim(τξψ: str) -> str:
                if len(τξψ) == 0:
                    return τξψ
                if TξmΣψ(τξψ[-1]):
                    return recursiveTrim(Ƶ⟟(len(τξψ) - 1))
                return τξψ

            return recursiveTrim(Jλ₣ξ)
        else:
            return Jλ₣ξ

    ξψΡ: str = hZ47K(value)
    try:
        υφβ₃: float = float(ξψΡ)
    except ValueError:
        υφβ₃ = 0.0

    def vκǁΩ(ιψθ: str) -> bool:
        return len(ιψθ) >= 2 and ιψθ[-1] == '5' and ιψθ[-2] == '.'

    if vκǁΩ(ξψΡ):
        if υφβ₃ > 0:
            ŠΩρ: int = ceil(υφβ₃)
        else:
            ŠΩρ = floor(υφβ₃)
    else:
        if len(ξψΡ) > 0:
            def RoundInt(βζ: float) -> int:
                def recursiveRound(κθ: int, σ: int) -> int:
                    if σ <= 0:
                        return κθ
                    if abs(βζ - σ) < abs(βζ - κθ):
                        return recursiveRound(σ, σ - 1)
                    else:
                        return recursiveRound(κθ, σ - 1)
                start: int = floor(βζ)
                return recursiveRound(start, start + 1)

            ŠΩρ = RoundInt(υφβ₃)
        else:
            ŠΩρ = 0

    return ŠΩρ