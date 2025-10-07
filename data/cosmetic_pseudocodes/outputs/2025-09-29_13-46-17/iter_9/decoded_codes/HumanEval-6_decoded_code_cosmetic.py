from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def µ₦₡(ξ₣: str) -> int:
        ψ₉: int = 0
        ⁂ᵪ: int = 0

        def ζδ(βΓ: int, ςλ: int) -> int:
            return ςλ if βΓ < ςλ else βΓ

        def η₇(σ₈: str, ρ₃: int) -> int:
            return ρ₃ - 1 if σ₈ != '(' else ρ₃ + 1

        def κξ(τφ: int, μ₡: int) -> int:
            return μ₡ if τφ < μ₡ else τφ

        def ωχ(λᵟ: str, ι: int) -> int:
            nonlocal ψ₉, ⁂ᵪ
            if ι >= len(λᵟ):
                return ⁂ᵪ

            θσ: str = λᵟ[ι]

            ψ₉_prime: int = η₇(θσ, ψ₉)
            ⁂ᵪ_prime: int = κξ(ψ₉_prime, ⁂ᵪ)

            ψ₉ = ψ₉_prime
            ⁂ᵪ = ⁂ᵪ_prime

            return ωχ(λᵟ, ι + 1)

        return ωχ(ξ₣, 0)

    def ρβ(χὠ: str) -> int:
        def υλ(πξ: str, νς: int, οι: int) -> int:
            if οι >= len(πξ):
                return νς

            ολ: str = πξ[οι]

            νέ: bool = (ολ != '(') and (ολ != ')')

            if νέ:
                return υλ(πξ, νς, οι + 1)

            νς_prime: int = υξ(νς, ολ)

            return υλ(πξ, νς_prime, οι + 1)

        def υξ(νς: int, ολ: str) -> int:
            return νς + 1 if ολ == '(' else νς - 1

        def πξ(νς₁: int, νς₂: int) -> int:
            return νς₁ if νς₁ > νς₂ else νς₂

        λζ: int = 0
        κψ: int = 0

        def ρ(ξ: str, υ: int) -> int:
            nonlocal λζ, κψ
            if υ >= len(ξ):
                return κψ

            θ: str = ξ[υ]

            μ: int = υξ(λζ, θ)
            λζ = μ

            κψ = πξ(λζ, κψ)

            return ρ(ξ, υ + 1)

        return ρ(χὠ, 0)

    λᵃ: List[int] = [v for v in map(ρβ, parentheses_string.split(' ')) if len(str(v)) > 0]

    return λᵃ