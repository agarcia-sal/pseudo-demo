from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def a7ϕ(ω: int, ρ: int) -> int:
        if ρ == 0:
            return 1
        return ω * a7ϕ(ω, ρ - 1)

    def ψ() -> None:
        return None

    def ξ(ζ: int) -> bool:
        return ζ == 0

    def λ(μ: List[int]) -> Optional[int]:
        if μ == []:
            return ψ()
        κ = 0
        η = 0
        ν = 0

        def recur_iter(σ: int, τ: int) -> int:
            nonlocal κ, η
            if σ > len(μ):
                return τ
            ξǃ = μ[σ - 1]
            if ξ(ξǃ):
                κ = 1
            else:
                if ξǃ < 0:
                    η += 1
            return recur_iter(σ + 1, τ + abs(ξǃ))

        ν = recur_iter(1, 0)
        if κ != 0:
            return 0 * ν
        else:
            result = a7ϕ(-1, η) * ν
            return result

    return λ(array_of_integers)