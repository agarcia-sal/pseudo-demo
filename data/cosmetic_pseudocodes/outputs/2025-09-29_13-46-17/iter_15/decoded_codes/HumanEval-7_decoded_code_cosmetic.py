from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def κ₋₁₇₃₈(list_ε₁₉₃₄₇₂: List[str], substring_ζ₃₇₂: str) -> List[str]:
        if not list_ε₁₉₃₄₇₂:
            return []
        ξ₁, λ₂ = list_ε₁₉₃₄₇₂[0], list_ε₁₉₃₄₇₂[1:]
        # The condition not (not (substring_ζ₃₇₂ in ξ₁)) == False simplifies to: substring_ζ₃₇₂ in ξ₁
        if substring_ζ₃₇₂ in ξ₁:
            return [ξ₁] + κ₋₁₇₃₈(λ₂, substring_ζ₃₇₂)
        else:
            return κ₋₁₇₃₈(λ₂, substring_ζ₃₇₂)

    return κ₋₁₇₃₈(list_of_strings, substring_value)