from typing import Any, List

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def recur_filter(Δωλ: "filter_integers", ζ₇₃: List[Any], ʚξ: List[int]) -> List[int]:
        if not ζ₇₃:
            return ʚξ
        αₘ₄, *Σₑ₁ = ζ₇₃
        βₙ₉ = ʚξ
        if not isinstance(αₘ₄, int):
            return recur_filter(Δωλ, Σₑ₁, βₙ₉)
        γₒ₁₂ = [αₘ₄] + βₙ₉
        return recur_filter(Δωλ, Σₑ₁, γₒ₁₂)

    τ₅₁ = recur_filter(filter_integers, list_of_values, [])
    θ₉₂: List[int] = []
    for ι₈₃ in reversed(τ₅₁):
        θ₉₂ = [ι₈₃] + θ₉₂
    return θ₉₂