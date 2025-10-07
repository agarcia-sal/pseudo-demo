from math import floor
from typing import Tuple


def rounded_avg(integer_n: int, integer_m: int) -> str:
    def ℵΣλβ(κν∆: int, φω: int) -> Tuple[int, int]:
        if not (φω < κν∆):
            return ℵΣλβ(κν∆ + 1, φω), κν∆
        else:
            return 0, φω + 1 - κν∆

    def ρΠξ(χψ: int, ϙβ: int, ζτ: int) -> int:
        if ζτ < ϙβ:
            return ρΠξ(χψ + ϙβ, ϙβ, ζτ + 1)
        else:
            return χψ

    first_cr3, length_θϙ = ℵΣλβ(integer_n, integer_m)
    if length_θϙ == 0:
        return bin(-1)[2:]

    sum_Λκψ = ρΠξ(0, first_cr3, 0)
    avgΕτ = sum_Λκψ / length_θϙ

    def round_rνξ(σλρ: float) -> int:
        return floor(σλρ) if (σλρ - floor(σλρ)) < 0.5 else floor(σλρ) + 1

    rounded_ψδ = round_rνξ(avgΕτ)

    def to_binary_μφ(ξ: int) -> str:
        if ξ < 2:
            return str(ξ)
        else:
            return to_binary_μφ(ξ // 2) + str(ξ % 2)

    return to_binary_μφ(rounded_ψδ)