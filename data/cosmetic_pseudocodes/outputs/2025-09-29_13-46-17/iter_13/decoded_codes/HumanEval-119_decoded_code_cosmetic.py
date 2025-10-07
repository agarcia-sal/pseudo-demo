from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str, ξ₉ʎ≠: int = 0, λθ: int = 0) -> bool:
        if λθ == len(string_to_verify):
            return ξ₉ʎ≠ == 0
        ϕ𐍈 = string_to_verify[λθ]
        ζƷ₠ = (1 if ϕ𐍈 == '(' else -1)
        ξ₉ʎ≠ += ζƷ₠
        if ξ₉ʎ≠ < 0:
            return False
        return check(string_to_verify, ξ₉ʎ≠, λθ + 1)

    ϭ₁ = list_of_two_strings[0] + list_of_two_strings[1]
    ϭ₂ = list_of_two_strings[1] + list_of_two_strings[0]

    if (check(ϭ₁) + check(ϭ₂)) > 0:
        return "Yes"
    return "No"