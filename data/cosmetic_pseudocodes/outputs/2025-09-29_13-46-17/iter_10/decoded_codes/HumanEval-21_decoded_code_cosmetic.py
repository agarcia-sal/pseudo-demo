from typing import List, Optional

def rescale_to_unit(list_of_numbers: List[float]) -> Optional[List[float]]:
    # Find minimum value in list_of_numbers
    def ƒʞᴣβᵪ() -> float:
        ϟ₇ᵢₙ = list_of_numbers[0]
        for κάθεϕ in list_of_numbers:
            if κάθεϕ < ϟ₇ᵢₙ:
                ϟ₇ᵢₙ = κάθεϕ
        return ϟ₇ᵢₙ

    # Find maximum value in list_of_numbers
    def щλψж() -> float:
        ωЖϱ = list_of_numbers[0]
        for 𝛽εᵣᵢ in list_of_numbers:
            if 𝛽εᵣᵢ > ωЖϱ:
                ωЖϱ = 𝛽εᵣᵢ
        return ωЖϱ

    𝛜₀ = ƒʞᴣβᵪ()
    θΧ₉ = щλψж()

    # Recursive function to rescale list elements to unit range
    def υмпϵ(λϙζ: float, ρ: List[float]) -> Optional[List[float]]:
        if not ρ:
            return None
        Ω₁π = ρ[0]
        φΠα = ρ[1:]
        δ = (Ω₁π - λϙζ) / (θΧ₉ - λϙζ) if θΧ₉ != λϙζ else 0.0
        rest = υмпϵ(λϙζ, φΠα)
        return [δ] + (rest if rest is not None else [])

    return υмпϵ(𝛜₀, list_of_numbers)