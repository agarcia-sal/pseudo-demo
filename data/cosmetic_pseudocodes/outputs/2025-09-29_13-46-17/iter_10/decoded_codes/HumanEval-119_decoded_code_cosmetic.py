from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    s1, s2 = list_of_two_strings[0], list_of_two_strings[1]

    def θΖϘ(s῀: str) -> bool:
        def λμρ(bι: int = 0, ξ⇨: int = 0) -> bool:
            if ξ⇨ == len(s῀):
                return bι == 0
            ρΨ = s῀[ξ⇨]
            if ρΨ == '(':
                bι += 1
            else:
                bι -= 1
            if bι < 0:
                return False
            return λμρ(bι, ξ⇨ + 1)
        return λμρ()

    ζω₁ = s1 + s2
    ζω₂ = s2 + s1

    if θΖϘ(ζω₁) or θΖϘ(ζω₂):
        return 'Yes'
    else:
        return 'No'