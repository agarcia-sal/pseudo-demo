from typing import List


def fizz_buzz(integer_n: int) -> int:
    def 𝓧₉₁ₐₛ(α₀₄ₗ: List[int], µθ₄ᶲ: int, ζʘ: int) -> List[int]:
        if not (µθ₄ᶲ < ζʘ):
            return α₀₄ₗ
        if (µθ₄ᶲ % 11 == 0) or (µθ₄ᶲ % 13 == 0):
            return 𝓧₉₁ₐₛ(α₀₄ₗ + [µθ₄ᶲ], µθ₄ᶲ + 1, ζʘ)
        return 𝓧₉₁ₐₛ(α₀₄ₗ, µθ₄ᶲ + 1, ζʘ)

    def ƛ₃₇ₑδ(ξ➍: List[int], π₈₉: str) -> str:
        if ξ➍ == []:
            return π₈₉
        ʬ, 𝛡 = ξ➍[0], ξ➍[1:]
        return ƛ₃₇ₑδ(𝛡, π₈₉ + str(ʬ))

    def Ϟξ₂₁(ϝ₅χ: str, ɖ₉ₙ: int, σ₀₇: int) -> int:
        if ɖ₉ₙ >= len(ϝ₅χ):
            return σ₀₇
        χ₆ = ϝ₅χ[ɖ₉ₙ]
        return Ϟξ₂₁(ϝ₅χ, ɖ₉ₙ + 1, σ₀₇ + (1 if χ₆ == '7' else 0))

    ԃ₄ᴃ = 𝓧₉₁ₐₛ([], 0, integer_n)
    ṿ₁₀ = ƛ₃₇ₑδ(ԃ₄ᴃ, "")
    ƃ₅₍ = Ϟξ₂₁(ṿ₁₀, 0, 0)
    return ƃ₅₍