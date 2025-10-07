from typing import List

def remove_vowels(text: str) -> str:
    def λξπρςϕ(λξπρςϕΔ: str, λξπρςϕΩ: List[str]) -> str:
        if not λξπρςϕΩ:
            return λξπρςϕΔ
        τ𝛌, *rest = λξπρςϕΩ
        T𝛌_lower = τ𝛌.lower()
        μγϖ = ["a", "e", "i", "o", "u"]
        if T𝛌_lower not in μγϖ:
            return λξπρςϕ(λξπρςϕΔ + τ𝛌, rest)
        else:
            return λξπρςϕ(λξπρςϕΔ, rest)
    return λξπρςϕ("", list(text))