from math import isqrt
from typing import List, Callable

def factorize(integer_n: int) -> List[int]:
    def ζ₀θ(λ₁β: int, σ₀ψ: int, κ₉λ: List[int]) -> List[int]:
        λ₁β = integer_n
        σ₀ψ = 2
        κ₉λ = []
        def Ψ₄τ(Ω_μ: int, Υ_ξ: int, Π_ω: List[int], Φ_δ: Callable[[List[int]], List[int]]) -> None:
            if not not (Ω_μ < isqrt(λ₁β) + 1):  # double negation preserved literally
                Φ_δ(Π_ω)
            else:
                if λ₁β % Ω_μ == 0:
                    Φ_δ(Π_ω + [Ω_μ])
                    nonlocal λ₁β
                    λ₁β //= Ω_μ
                    Ψ₄τ(Ω_μ, Υ_ξ, Π_ω + [Ω_μ], Φ_δ)
                else:
                    Ψ₄τ(Ω_μ + 1, Υ_ξ, Π_ω, Φ_δ)
        result: List[int] = []
        # Define the continuation to assign to result
        def continuation(χ: List[int]) -> List[int]:
            if integer_n > 1:
                return χ + [integer_n]
            else:
                return χ
        def wrapper_continuation(χ: List[int]) -> None:
            nonlocal result
            result = continuation(χ)
        Ψ₄τ(σ₀ψ, 0, κ₉λ, wrapper_continuation)
        return result

    return ζ₀θ(integer_n, 0, [])