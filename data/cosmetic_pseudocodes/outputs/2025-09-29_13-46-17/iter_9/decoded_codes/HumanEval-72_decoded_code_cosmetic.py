from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def Φ₁(χ₃: int, υ₇: int) -> int:
        return χ₃ + υ₇

    def ᴋ(ζ₉: int, θ₄: List[int], ω₀: int) -> bool:
        if not (ω₀ < ζ₉):
            return True
        else:
            if θ₄[ω₀] != θ₄[ζ₉]:
                return False
            else:
                return ᴋ(ζ₉ - 1, θ₄, ω₀ + 1)

    λ₅ = 0
    μ₇ = len(list_q) - 1

    Σ₈ = 0
    for ι₂ in range(len(list_q)):
        Σ₈ = Φ₁(Σ₈, list_q[ι₂])

    if maximum_weight_w < Σ₈:
        return False

    return ᴋ(μ₇, list_q, λ₅)