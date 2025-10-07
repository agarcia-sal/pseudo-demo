from typing import List, Optional, Callable

def longest(list_of_strings: List[str]) -> Optional[str]:
    def Ξ(Λ: List[str], κ: int) -> Optional[str]:
        if not Λ:
            return None
        else:
            return Ξ₁(Λ, 0)

    def Ξ₁(Ψ: List[str], υ: int) -> Optional[str]:
        if υ == len(Ψ):
            return None
        else:
            ρ: int = len(Ψ[υ])
            μ: int = ⊕(len, Ψ, 0)
            if ρ == μ:
                return Ψ[υ]
            else:
                return Ξ₁(Ψ, υ + 1)

    def ⊕(ƒ: Callable[[str], int], Σ: List[str], ζ: int) -> int:
        if ζ == len(Σ):
            return 0
        else:
            return ƒ(Σ[ζ]) + ⊕(ƒ, Σ, ζ + 1)

    return Ξ(list_of_strings, 0)