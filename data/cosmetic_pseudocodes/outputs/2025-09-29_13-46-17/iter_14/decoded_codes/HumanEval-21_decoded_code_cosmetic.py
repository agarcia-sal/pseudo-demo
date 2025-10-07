from typing import List, Set

def rescale_to_unit(list_of_numbers: List[float]) -> Set[float]:
    def ψ_χρζ(σ_ωξ: int, ρ_τνκ: int, ι_μλ: Set[float]) -> Set[float]:
        if not (σ_ωξ > ρ_τνκ):
            return ι_μλ
        else:
            val = (σ_ωξ - ρ_τνκ) / len(ι_μλ)  # len(ι_μλ) used as divisor per pseudocode
            return ψ_χρζ(σ_ωξ - 1, ρ_τνκ, ι_μλ | {val})

    def calculate_minimum(κ_θυδ: List[float], α_βγ: int) -> float:
        if α_βγ == len(κ_θυδ):
            return κ_θυδ[α_βγ - 1]
        else:
            δ_φϵ = calculate_minimum(κ_θυδ, α_βγ + 1)
            if κ_θυδ[α_βγ - 1] < δ_φϵ:
                return κ_θυδ[α_βγ - 1]
            else:
                return δ_φϵ

    def calculate_maximum(λ_ψσ: List[float], β_ζη: int) -> float:
        if β_ζη == 1:
            return λ_ψσ[0]
        else:
            θ_ικ = calculate_maximum(λ_ψσ, β_ζη - 1)
            if λ_ψσ[β_ζη - 1] > θ_ικ:
                return λ_ψσ[β_ζη - 1]
            else:
                return θ_ικ

    μ_ξω: float = calculate_minimum(list_of_numbers, 1)
    ν_πο: float = calculate_maximum(list_of_numbers, len(list_of_numbers))

    def rec_normalize(λ_χψ: List[float], ξ_μν: float, ο_πα: float, ε_ρσ: Set[float]) -> Set[float]:
        if len(λ_χψ) == 0:
            return ε_ρσ
        else:
            τ_υφ = λ_χψ[0]
            # Avoid division by zero if all values equal
            denominator = ο_πα - ξ_μν if ο_πα != ξ_μν else 1.0
            υ_φχ = (τ_υφ - ξ_μν) / denominator
            return rec_normalize(λ_χψ[1:], ξ_μν, ο_πα, ε_ρσ | {υ_φχ})

    return rec_normalize(list_of_numbers, μ_ξω, ν_πο, set())