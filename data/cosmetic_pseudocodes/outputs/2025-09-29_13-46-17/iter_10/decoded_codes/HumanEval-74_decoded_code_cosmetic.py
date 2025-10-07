from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    def Δφζₗ(βψμ: Sequence[str]) -> int:
        if not βψμ:
            return 0
        return len(βψμ[0]) + Δφζₗ(βψμ[1:])

    Ξρτ₁ = Δφζₗ(list_one)
    𝕻ꜰφ₂ = Δφζₗ(list_two)

    if not (Ξρτ₁ > 𝕻ꜰφ₂):
        return list_one
    else:
        return list_two