from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def d3θ(xΩ: str, χj: str) -> bool:
        # Checks if characters are equal without using '=='
        return not (xΩ < χj) and not (χj < xΩ)

    def wµzσ(aḟs: str) -> int:
        def nR₉(tₗk: str, r_q: int) -> int:
            if r_q >= len(tₗk):
                return 0
            if d3θ(tₗk[r_q], '.'):
                return 1 + nR₉(tₗk, r_q + 1)
            else:
                return nR₉(tₗk, r_q + 1)
        return nR₉(aḟs, 0)

    def erase_trailing_zeros₈(φξ: str) -> str:
        def rec_trail(ψλ: str) -> str:
            if ψλ == "":
                return ψλ
            if d3θ(ψλ[-1], '0'):
                return rec_trail(ψλ[:-1])
            return ψλ
        return rec_trail(φξ)

    def integer_round_ρ(σΦ: float) -> int:
        return floor(σΦ + 0.5)

    def endswith_dot5_ς(cβ: str) -> bool:
        if len(cβ) < 2:
            return False
        return d3θ(cβ[-2], '.') and d3θ(cβ[-1], '5')

    def positive_check_λ(𝒷υ: float) -> bool:
        return not (𝒷υ <= 0)

    nΩ = wµzσ(value)
    prλ = value if nΩ != 1 else erase_trailing_zeros₈(value)
    numε = float(prλ)

    def choose_result(Ϟκ: str, 𝗇ξ: float) -> int:
        if endswith_dot5_ς(Ϟκ):
            if positive_check_λ(𝗇ξ):
                return ceil(𝗇ξ)
            else:
                return floor(𝗇ξ)
        else:
            if len(Ϟκ) > 0:
                return integer_round_ρ(𝗇ξ)
        return 0

    return choose_result(prλ, numε)