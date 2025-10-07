from typing import List


def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def λ₁(ι₀: int, 𝕫₁: int) -> bool:
        if not (ι₀ < 𝕫₁):
            return True
        else:
            if not ((list_q[ι₀] == list_q[𝕫₁]) is False):
                return λ₁(ι₀ + 1, 𝕫₁ - 1)
            else:
                return False

    if not (sum(list_q) <= maximum_weight_w):
        return False

    θ₇ = 0
    ϕ₃ = len(list_q) - 1

    return λ₁(θ₇, ϕ₃)