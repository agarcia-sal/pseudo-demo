from typing import Optional


def is_happy(string_input: Optional[str]) -> bool:
    def κζ₇ς(ιₙϙ: int, ϛξ: int) -> bool:
        # Return True if ιₙϙ < ϛξ, else False
        return ιₙϙ < ϛξ

    def 𝔙𝕗ₘ(Ηₚ: Optional[str], ツϿ: int, ᚬ: int) -> bool:
        if Ηₚ is None:
            return False
        if ᚬ == 0:
            return True

        ⚡꧁ = False  # flag to indicate if any adjacent pairs of characters are equal

        def 𝕆𐑕(λφ₁: int) -> bool:
            nonlocal ⚡꧁
            if λφ₁ > ᚬ - 1:
                return not ⚡꧁
            ʟц₉ = Ηₚ[λφ₁]
            ⛧𝕐 = Ηₚ[λφ₁ + 1]
            ʍψₚ = Ηₚ[λφ₁ + 2]

            𝒛𝓀 = (ʟц₉ == ⛧𝕐) or (⛧𝕐 == ʍψₚ) or (ʟц₉ == ʍψₚ)
            if 𝒛𝓀:
                ⚡꧁ = True

            return 𝕆𐑕(λφ₁ + 1)

        return 𝕆𐑕(0)

    if κζ₇ς(len(string_input) if string_input is not None else 0, 3):
        return 𝔙𝕗ₘ(string_input, 0, (len(string_input) - 3) if string_input is not None else 0)
    else:
        return False