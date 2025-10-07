from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def χ(ι: int, τ: int) -> int:
            if τ == len(ι_):  # Comparing with length of string stored externally
                return ι
            return χ(ι + 1 if ι_[τ] == '(' else ι - 1, τ + 1)

        ι_ = string_to_verify  # To make ι_ available inside χ
        ψ = χ(0, 0)
        return ψ == 0  # If the net count is zero, parentheses match

    ι₁: List[str] = [ch for ch in list_of_two_strings[0]]
    ι₂: List[str] = [ch for ch in list_of_two_strings[1]]
    μ_α: List[str] = ι₁ + ι₂
    ν_β: List[str] = ι₂ + ι₁

    if check("".join(μ_α)) or check("".join(ν_β)):
        return 'Yes'
    return 'No'