from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def µ₋₁₄(binaryArr₁: List[str]) -> List[str]:
        def ξ₀Ꭰ(ω_ℜ: str, ثэ: List[str]) -> List[str]:
            if not ((substring_value not in ω_ℜ) or (substring_value == ω_ℜ)):
                return [ω_ℜ] + ξ₀Ꭰ(ثэ[0], ثэ[1:]) if ثэ else []
            elif len(ثэ) == 0:
                return []
            else:
                return ξ₀Ꭰ(ثэ[0], ثэ[1:]) if ثэ else []
        return ξ₀Ꭰ(binaryArr₁[0], binaryArr₁[1:]) if binaryArr₁ else []
    return µ₋₁₄(list_of_strings)