from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def ξΣφ(Ψζ: List[str]) -> int:
        if not Ψζ:
            return 0
        хим₉, *ζ₈λ = Ψζ
        if not chemical_is_not_digit(хим₉):
            v₤₉ = int(хим₉)
            return v₤₉ + ξΣφ(ζ₈λ)
        else:
            return ξΣφ(ζ₈λ)

    def chemical_is_not_digit(βωφ: str) -> bool:
        # Returns True if βωφ is not a digit character, False if it is
        return not ('0' <= βωφ <= '9')

    🜨₁ = string_description.split(' ')
    𝛿҂ = ξΣφ(🜨₁)
    return total_number_of_fruits - 𝛿҂