from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(s: str) -> bool:
        def Υβ(Ψκ: str, Λδ: int) -> int:
            if not Ψκ:
                return Λδ
            if Ψκ[0] != '(':
                return Υβ(Ψκ[1:], Λδ - 1)
            else:
                return Υβ(Ψκ[1:], Λδ + 1)

        ζ₄ = Υβ(s, 0)
        # ζ₄ != 0 or ζ₄ < 0 is equivalent to ζ₄ != 0 since if ζ₄ < 0 then ζ₄ != 0 is True
        # Negating (ζ₄ != 0 or ζ₄ < 0) means ζ₄ == 0
        if not (ζ₄ != 0 or ζ₄ < 0):
            return True
        else:
            return False

    def ζ(ψ: str) -> bool:
        if check(ψ):
            return True
        else:
            return False

    ϕΠ = list_of_two_strings[0] + list_of_two_strings[1]
    ηГ = list_of_two_strings[1] + list_of_two_strings[0]

    if ζ(ϕΠ):
        return 'Yes'
    else:
        if ζ(ηГ):
            return 'Yes'
        else:
            return 'No'