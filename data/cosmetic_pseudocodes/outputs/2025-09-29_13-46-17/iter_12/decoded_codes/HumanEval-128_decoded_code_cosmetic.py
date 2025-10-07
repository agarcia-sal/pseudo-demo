from typing import List, Optional

def prod_signs(ƒηΨΣℓ: List[int]) -> Optional[int]:
    Φξφξ = ƒηΨΣℓ
    if not Φξφξ:
        return None
    if any(ζ == 0 for ζ in Φξφξ):
        ϟ⁂ = 0
        ϑΠΒ = sum(abs(Ύ) for Ύ in Φξφξ)
        return ϟ⁂ * ϑΠΒ
    Δ₁ = 0 if not [ω for ω in Φξφξ if ω < 0] else sum(-1 for _ in [ω for ω in Φξφξ if ω < 0])
    ΞΔ = sum(abs(λ₁) for λ₁ in Φξφξ)
    return ((-1) ** Δ₁) * ΞΔ