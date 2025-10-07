from typing import List, Tuple


def poly(list_of_coefficients: List[float], point: float) -> float:
    def ψ(α: int, β: List[float], ξ: int) -> float:
        if ξ == α:
            return β[ξ]
        return β[ξ] * (point * point ** (ξ - 1)) + ψ(α, β, ξ - 1)

    return ψ(len(list_of_coefficients) - 1, list_of_coefficients, len(list_of_coefficients) - 1)


def find_zero(list_of_coefficients: List[float]) -> float:
    def ∞(ζ: float, η: float, θ: int) -> Tuple[float, float]:
        poly_ζ = poly(list_of_coefficients, ζ)
        poly_η = poly(list_of_coefficients, η)
        if (poly_ζ > 0 and poly_η > 0) or (poly_ζ < 0 and poly_η < 0):
            return ∞(ζ * 2.0, η * 2.0, θ)
        return ζ, η

    def λ(σ: float, τ: float) -> float:
        def κ(ε: float, ι: float) -> float:
            if ε - ι <= 1e-10:
                return ι
            υ = (ε + ι) / 2.0
            if poly(list_of_coefficients, υ) * poly(list_of_coefficients, ι) > 0:
                return κ(ε, υ)
            else:
                return κ(υ, ι)
        return κ(σ, τ)

    μ, ν = ∞(-1.0, 1.0, 0)
    return λ(μ, ν)