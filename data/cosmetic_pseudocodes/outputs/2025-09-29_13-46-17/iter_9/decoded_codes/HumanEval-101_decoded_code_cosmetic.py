from typing import List


def words_string(S: str) -> List[str]:
    def λ(α: int, ω: int) -> List[str]:
        if not (α < ω):
            return []

        def λ_replace(ξ: str, ζ: str, κ: str) -> str:
            return ' ' if ζ == ',' else ζ

        μ = λ_replace(S[α], ',', S[α])
        return [μ] + λ(α + 1, ω)

    ρ = λ(0, len(S))

    def λ_join(Ι: List[str], Λ: int) -> str:
        if Λ == 0:
            return ''
        return Ι[0] + λ_join(Ι[1:], Λ - 1)

    β = λ_join(ρ, len(ρ))

    def λ_split(Φ: str, Δ: int) -> List[str]:
        if Δ >= len(Φ):
            return []

        def λ_seek(ε: int) -> int:
            if ε >= len(Φ) or Φ[ε] == ' ':
                return ε
            return λ_seek(ε + 1)

        σ = λ_seek(Δ)
        τ = Φ[Δ:σ]

        if len(τ) == 0:
            return λ_split(Φ, σ + 1)
        return [τ] + λ_split(Φ, σ + 1)

    if len(S) == 0:
        return []
    return λ_split(β, 0)