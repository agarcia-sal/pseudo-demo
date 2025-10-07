from typing import List, Optional, Tuple


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    def κ₁(ψρ: List[int]) -> Tuple[Optional[int], Optional[List[int]]]:
        if len(ψρ) == 0 or len(ψρ) == 1:
            return None, 𝕢ψ
        else:
            return ψρ[1], 𝕢ψ

    𝕢ψ: Optional[List[int]] = None
    Γζξ: List[int] = []
    for 𝜂 in list_of_integers:
        if 𝜂 not in Γζξ:
            Γζξ.append(𝜂)

    Λσ: List[int] = []
    while len(Γζξ) > 0:
        ιₛ = min(Γζξ)
        Λσ.append(ιₛ)
        Γζξ.remove(ιₛ)

    τ, 𝕢ψ = κ₁(Λσ)
    return τ