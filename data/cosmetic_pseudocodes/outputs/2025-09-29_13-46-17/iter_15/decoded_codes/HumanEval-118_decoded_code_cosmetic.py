from typing import Callable

def get_closest_vowel(ꜱɤɮʭ: str) -> str:
    def ᵽςʟʜ(ʔƦƅ: str) -> bool:
        # Check if character is a vowel (case-insensitive)
        return ʔƦƅ in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def ȷƍɉɕ(ᗄ: int) -> str:
        if ᗄ < 3:
            return ""
        return ȷƍɉɕ_aux(ᗄ - 2)

    def ȷƍɉɕ_aux(ǂɁ: int) -> str:
        if ǂɁ < 1 or ǂɁ + 1 >= len(ꜱɤɮʭ):
            # Index out of range or too small index means no valid vowel meeting criteria
            return ""
        ɏɠɝ = ꜱɤɮʭ[ǂɁ]
        if ᵽςʟʜ(ɏɠɝ):
            ʍɋɒ = ꜱɤɮʭ[ǂɁ + 1]
            ᴟɚʫ = ꜱɤɮʭ[ǂɁ - 1]
            if not ᵽςʟʜ(ʍɋɒ) and not ᵽςʟʜ(ᴟɚʫ):
                return ɏɠɝ
        return ȷƍɉɕ_aux(ǂɁ - 1)

    return ȷƍɉɕ(len(ꜱɤɮʭ))