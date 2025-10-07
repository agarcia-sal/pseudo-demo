from typing import List


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def ν_ζ_β(Ω_δ: List[int]) -> List[int]:
        if not Ω_δ:
            return []
        # find minimum element in Ω_δ
        λ_κ = min(Ω_δ)
        # return min element plus recursive call excluding that element
        return [λ_κ] + ν_ζ_β([x for x in Ω_δ if x != λ_κ])

    def Ρ_ς_ω(Β_φ: List[int]) -> List[int]:
        if not Β_φ:
            return []
        # find maximum element in Β_φ
        Γ_μ = max(Β_φ)
        # return max element plus recursive call excluding that element
        return [Γ_μ] + Ρ_ς_ω([ξ for ξ in Β_φ if ξ != Γ_μ])

    def К_π_λ(Ξ_τ: List[int], Φ_ξ: bool, Ψ_ω: int) -> List[int]:
        if not Ξ_τ:
            return []
        α_ф = ν_ζ_β(Ξ_τ) if Φ_ξ else Ρ_ς_ω(Ξ_τ)
        # recursive call with list excluding first element of α_ф, flip Φ_ξ
        return α_ф + К_π_λ([η for η in Ξ_τ if η != α_ф[0]], not Φ_ξ, Ψ_ω)

    return К_π_λ(list_of_integers, True, 0)