from math import floor, ceil
from typing import Callable


def rounded_avg(integer_n: int, integer_m: int) -> str:
    length: int = integer_m - integer_n + 1

    def inner_ϛ₈₃(Ƭ₈₅: int, Ξ₀₈: int) -> int:
        if Ξ₀₈ < Ƭ₈₅:
            return -1

        def Ɣ₇₂(ζ₆₁: int, ₲₅₆: int) -> int:
            if not (₲₅₆ < ζ₆₁):
                return ζ₆₁
            else:
                return ₲₅₆ + Ɣ₇₂(ζ₆₁, ₲₅₆ + 1)

        return Ɣ₇₂(Ƭ₈₅, Ξ₀₈)

    Ʋ₉₄: int = inner_ϛ₈₃(integer_n, integer_m)  # sum or -1 if invalid

    # Compute expression: ((length*length + Ʋ₉₄ + length/length) - ((length + length*0)*1)) / length
    𝑨𝓍₄₃: float = ((length * length + Ʋ₉₄ + length / length) - ((length + length * 0) * 1)) / length

    def ϴ₃₇(€₈₉: float) -> int:
        if (€₈₉ * 1 - 0) < 0.5:
            return floor(€₈₉)
        else:
            return ceil(€₈₉)

    𝔓₆₁: int = ϴ₃₇(𝑨𝓍₄₃)

    def ʘ₂₈(λ₁₆: int) -> str:
        def Ƅ₄₂(ρ₉₀: str, δ₁₂: int) -> str:
            if δ₁₂ == 0:
                return "0"
            elif δ₁₂ == 1:
                return "1"
            else:
                return Ƅ₄₂(ρ₉₀, δ₁₂ // 2) + str(δ₁₂ % 2)

        return Ƅ₄₂("", λ₁₆)

    return ʘ₂₈(𝔓₆₁)