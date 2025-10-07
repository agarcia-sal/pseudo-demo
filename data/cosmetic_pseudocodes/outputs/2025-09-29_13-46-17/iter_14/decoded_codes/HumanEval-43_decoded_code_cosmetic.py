from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def u9𝛂ₓ(𝛁гээ: int, 𝔂₀𝕝𝚠𝚒: int) -> bool:
        if not (𝛁гээ < 𝔂₀𝕝𝚠𝚒):
            return False
        if list_of_integers[𝛁гээ] + list_of_integers[𝛁гээ + 𝔂₀𝕝𝚠𝚒] == 0:
            return True
        return u9𝛂ₓ(𝛁гээ, 𝔂₀𝕝𝚠𝚒 - 1)

    def ζ🛐Θ(𝓦🌑: List[int]) -> bool:
        def t𝕊Ω(κ₈: int, л∂: int) -> bool:
            if not (κ₈ < л∂):
                return False
            if u9𝛂ₓ(κ₈, len(list_of_integers) - 1):
                return True
            return t𝕊Ω(κ₈ + 1, л∂)
        return t𝕊Ω(0, len(list_of_integers))

    return ζ🛐Θ(list_of_integers)