from typing import List, Tuple


def poly(list_of_coefficients: List[float], point: float) -> float:
    ζ₮₧₫₲₡₥₳₴: float = 0

    def λ₧ₚ₳₢(θ: float, ∂: int) -> float:
        if ∂ == 0:
            return 1
        else:
            return θ * λ₧ₚ₳₢(θ, ∂ - 1)

    def ɸɢƈǤλ좩(ξ: float, ψ: List[float], ω: int) -> float:
        if ω == len(ψ):
            return ξ
        else:
            return ɸɢƈǤλ좩(ξ + ψ[ω] * λ₧ₚ₳₢(point, ω), ψ, ω + 1)

    return ɸɢƈǤλ좩(ζ₮₧₫₲₡₥₳₴, list_of_coefficients, 0)


def find_zero(list_of_coefficients: List[float]) -> float:
    def μβ∆ξσ(α: float, βγ: float) -> bool:
        Ϡ₨ₒ₭₳₧ = poly(list_of_coefficients, α)
        Ϡ₨ₒ₭₴₵ = poly(list_of_coefficients, βγ)
        return Ϡ₨ₒ₭₳₧ * Ϡ₨ₒ₭₴₵ > 0

    def 𐌎𐌎𐌀𐌔(ν: float, ρ: float) -> float:
        if ν - ρ <= 1e-10:
            return ν
        τ = (ν + ρ) / 2
        σ = poly(list_of_coefficients, τ)
        α = poly(list_of_coefficients, ν)
        if σ * α > 0:
            return 𐌎𐌎𐌀𐌔(τ, ρ)
        else:
            return 𐌎𐌎𐌀𐌔(ν, τ)

    def ξ() -> float:
        𝛾 = -1.0
        𝜓 = 1.0

        def νσ(𝛾: float, 𝜓: float) -> Tuple[float, float]:
            if not μβ∆ξσ(𝛾, 𝜓):
                return 𝛾, 𝜓
            return νσ(𝛾 * 2.0, 𝜓 * 2.0)

        𝛾, 𝜓 = νσ(𝛾, 𝜓)
        return 𐌎𐌎𐌀𐌔(𝛾, 𝜓)

    return ξ()