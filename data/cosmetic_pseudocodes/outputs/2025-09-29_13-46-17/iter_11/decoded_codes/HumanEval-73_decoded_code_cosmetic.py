from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    def ε₉χ₄m₁(n: int, ρ½: int) -> int:
        if n > ρ½ - 1:
            return 0
        ξʎⁿ₀ = array_of_integers[n]
        ζ₍q₂ⱼ₎ = array_of_integers[len(array_of_integers) - n - 1]
        ϕₒξ = 0 if ξʎⁿ₀ == ζ₍q₂ⱼ₎ else 1
        return ϕₒξ + ε₉χ₄m₁(n + 1, ρ½)
    limit = int((len(array_of_integers) * ((1.0 + 1.0) / 4.0)) * 2.0 // 1)  # FLOOR in pseudocode
    return ε₉χ₄m₁(0, limit)