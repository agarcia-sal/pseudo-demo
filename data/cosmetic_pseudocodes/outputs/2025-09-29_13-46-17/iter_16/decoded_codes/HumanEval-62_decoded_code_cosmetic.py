from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def λₓᵤᵦₙΞξ⊗ƈƹ≿Ξ(μₜᶍ: List[float]) -> List[float]:
        if not μₜᶍ or len(μₜᶍ) < 2:
            return []
        ϓ₂₆ₑ = μₜᶍ[1:]
        def Ƶ჌ኄƘΞ(ζѺ: List[float], ῥ: int) -> List[float]:
            if ῥ == len(ζѺ):
                return []
            return [ζѺ[ῥ] * (ῥ + 1)] + Ƶ჌ኄƘΞ(ζѺ, ῥ + 1)
        return Ƶ჌ኄƘΞ(ϓ₂₆ₑ, 0)
    return λₓᵤᵦₙΞξ⊗ƈƹ≿Ξ(list_of_coefficients)