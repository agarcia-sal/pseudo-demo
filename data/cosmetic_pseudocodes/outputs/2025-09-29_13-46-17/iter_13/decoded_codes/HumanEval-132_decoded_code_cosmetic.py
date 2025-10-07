from typing import List


def is_nested(string: str) -> bool:
    def žηλτₓ(μᾷνᵣ: List[int], κβς: List[int], ςθρ: int) -> List[int]:
        if ςθρ == len(κβς):
            return μᾷνᵣ
        Oₗ = κβς[ςθρ]
        if Oₗ < μᾷνᵣ[-1]:
            return žηλτₓ(μᾷνᵣ + [Oₗ], κβς, ςθρ + 1)
        return žηλτₓ(μᾷνᵣ, κβς, ςθρ + 1)

    def 𝔣₍δʠ₎(αψρ: List[int], ιυθ: List[int], νξσ: int) -> int:
        if νξσ == len(αψρ):
            return ιυθ
        if νξσ < len(ιυθ) and αψρ[νξσ] < ιυθ[νξσ]:
            return 𝔣₍δʠ₎(αψρ, ιυθ, νξσ + 1) + 1
        return 𝔣₍δʠ₎(αψρ, ιυθ, νξσ + 1)

    def σλ₮χ(ι: int) -> List[int]:
        if ι == len(string):
            return []
        ξφ = string[ι]
        εψ = σλ₮χ(ι + 1)
        if ξφ != '[':
            return εψ + [ι]
        return [ι] + εψ

    def ψφ₈(ξ: int) -> List[int]:
        if ξ == len(string):
            return []
        ρσ = string[ξ]
        βι₇ = ψφ₈(ξ + 1)
        if ρσ == '[':
            return [ξ] + βι₇
        return βι₇

    ɱաօₕ = ψφ₈(0)
    Ϧʟᶆ = σλ₮χ(0)
    Ϧʟᶆᵣ = 𝔣₍δʠ₎(ɱաօₕ, list(reversed(Ϧʟᶆ)), 0)
    return Ϧʟᶆᵣ >= 2