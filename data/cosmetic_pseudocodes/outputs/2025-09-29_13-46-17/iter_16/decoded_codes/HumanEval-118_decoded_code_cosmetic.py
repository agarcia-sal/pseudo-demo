from typing import Literal


def get_closest_vowel(word: str) -> str:
    vowels: set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    def ƒ𝛿₁(𝛽μκ: str, ɸ: int) -> str:
        if ɸ <= 0:
            return ""
        if 𝛽μκ[ɸ] in vowels:
            # Check neighbors safely:
            prev_char = 𝛽μκ[ɸ - 1] if ɸ - 1 >= 0 else ""
            next_char = 𝛽μκ[ɸ + 1] if ɸ + 1 < len(𝛽μκ) else ""
            if (prev_char not in vowels) and (next_char not in vowels):
                return 𝛽μκ[ɸ]
            return ƒ𝛿₁(𝛽μκ, ɸ - 1)
        return ƒ𝛿₁(𝛽μκ, ɸ - 1)

    𝛴ΞΛ = len(word) - 2
    Ɓπϵ = ""
    return Ɓπϵ if len(word) < 3 else ƒ𝛿₁(word, 𝛴ΞΛ)