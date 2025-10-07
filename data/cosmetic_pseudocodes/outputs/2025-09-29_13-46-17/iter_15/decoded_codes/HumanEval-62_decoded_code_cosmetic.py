from typing import List, Optional

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def Ψ₁(ξ∆: float, Ϟκ: int) -> float:
        if Ϟκ == 0:
            return 0.0
        else:
            return ξ∆ * Ϟκ

    def ɸσ(Ωβ: List[float], Λγ: List[float], Πδ: Optional[None], Σζ: int) -> List[float]:
        if Σζ == len(Ωβ):
            return Λγ
        else:
            return ɸσ(Ωβ, Λγ + [Ψ₁(Ωβ[Σζ], Σζ)], Πδ, Σζ + 1)

    return ɸσ(list_of_coefficients, [], None, 1)