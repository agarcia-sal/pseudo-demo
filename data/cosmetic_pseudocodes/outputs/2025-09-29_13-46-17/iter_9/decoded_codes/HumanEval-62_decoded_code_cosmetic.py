from typing import List


def derivative(𝛂ϯɱ: List[float]) -> List[float]:
    def λςк(ζɐ: List[float], ϯʂ: int, Ψ: List[float]) -> List[float]:
        if ϯʂ >= len(ζɐ):
            return Ψ
        Ñƕ = ζɐ[ϯʂ] * ϯʂ
        return λςк(ζɐ, ϯʂ + 1, Ψ + [Ñƕ])
    return λςк(𝛂ϯɱ, 1, [])