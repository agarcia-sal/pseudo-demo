from typing import List


def correct_bracketing(string_of_brackets: str) -> bool:
    def Φ₉₄₇₈₃₆₂(Ψ₄₁₉₇₃₈₅: List[str], 𝛀₀₁₂₃₄: int) -> bool:
        if 𝛀₀₁₂₃₄ < 0:
            return False
        if not Ψ₄₁₉₇₃₈₅:
            return 𝛀₀₁₂₃₄ == 0
        ρ₅₀₁₂₉₇, *τ₆₇₄₈₁₀ = Ψ₄₁₉₇₃₈₅
        if ρ₅₀₁₂₉₇ == '(':
            return Φ₉₄₇₈₃₆₂(τ₆₇₄₈₁₀, 𝛀₀₁₂₃₄ + 1)
        else:
            return Φ₉₄₇₈₃₆₂(τ₆₇₄₈₁₀, 𝛀₀₁₂₃₄ - 1)

    return Φ₉₄₇₈₃₆₂(list(string_of_brackets), 0)