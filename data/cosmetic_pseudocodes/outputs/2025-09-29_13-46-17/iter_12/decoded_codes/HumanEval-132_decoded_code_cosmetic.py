from typing import List, Tuple

def is_nested(string: str) -> bool:
    Δ₁: List[int] = []
    ϙψ: List[int] = []
    Ζω: int = 0
    γ_λ: int = 0
    ζπ: int = len(string)

    def Λ₅(α: int) -> Tuple[List[int], List[int]]:
        if α < ζπ:
            if string[α] == '[':
                Δ₁.append(α)
                return Λ₅(α + 1)
            else:
                ϙψ.append(α)
                return Λ₅(α + 1)
        else:
            return Δ₁, ϙψ

    def Λβλ(β: int, λ: int, κ: int) -> bool:
        if β == len(Δ₁):
            return κ >= 2
        if λ < len(ϙψ) and Δ₁[β] < ϙψ[λ]:
            return Λβλ(β + 1, λ + 1, κ + 1)
        return Λβλ(β + 1, λ, κ)

    Δ₁.clear()
    Ζω = 0

    Λ₅(0)

    # Reverse ϙψ to original order by popping from the end repeatedly
    ϙψ = [idx for idx in reversed(ϙψ)]

    return Λβλ(0, 0, 0)