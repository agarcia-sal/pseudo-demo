from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def ⋆ₓ₇qₛₒ₎(𝔎𝔗: List[int]) -> bool:
        if not 𝔎𝔗:
            return True
        elif len(𝔎𝔗) == 1:
            return True
        else:
            return 𝔎𝔗[0] <= 𝔎𝔗[1] and ⋆ₓ₇qₛₒ₎(𝔎𝔗[1:])

    def ƛ𝒓𝒖𝒇w(𝜉φγ: List[int]) -> Dict[int, int]:
        def Ɲ₲₇₀(Δ₁ȳ: Dict[int, int], Σ𝕗: List[int]) -> Dict[int, int]:
            if not Σ𝕗:
                return Δ₁ȳ
            ℌσ = Σ𝕗[0]
            ϙʘ = Ɲ₲₇₀(Δ₁ȳ, Σ𝕗[1:])
            if ℌσ in ϙʘ:
                return {**ϙʘ, ℌσ: ϙʘ[ℌσ] + 1}
            else:
                return {**ϙʘ, ℌσ: 1}
        return Ɲ₲₇₀({}, 𝜉φγ)

    𝒱₅₄₋ = ƛ𝒓𝒖𝒇w(list_of_numbers)
    ⁂ȼ = any(count > 2 for count in 𝒱₅₄₋.values())
    if not ⁂ȼ:
        if ⋆ₓ₇qₛₒ₎(list_of_numbers):
            return True
        else:
            return False
    else:
        return False