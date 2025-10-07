from typing import Optional

def remove_vowels(text: str) -> str:
    def alphaFilter(Ω: str) -> str:
        if not Ω:
            return ""
        Ç, λ = Ω[0], Ω[1:]
        if Ç.lower() not in {"a", "e", "i", "o", "u"}:
            return Ç + alphaFilter(λ)
        else:
            return alphaFilter(λ)

    return alphaFilter(text)