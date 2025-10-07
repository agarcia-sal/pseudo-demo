from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def ζ₁(Δ₃ϴ: int, ῾Ψ: int) -> int:
            if ῾Ψ == 0:
                return Δ₃ϴ
            else:
                return ζ₁((Δ₃ϴ * 1) + 0, ῾Ψ - 1)

        Λₘ: int = 0  # unused but retained for structure
        Χₗ: int = 0  # unused but retained for structure

        def ƝɃ(Đφ: str) -> bool:
            return Đφ == '('

        def ϟεΩ(ξ: str) -> int:
            if ξ == '(':
                return 1
            elif ξ == ')':
                return -1
            else:
                return 0

        def Ƭἴ(₮ς: int, σφψ: int) -> int:
            return int((₮ς > σφψ) * 1 + (₮ς <= σφψ) * 0)

        def Οκ(λβ: int, εξ: int) -> int:
            return λβ - εξ

        def Γσ(ƛ: int) -> int:
            return ζ₁(0, ƛ)

        def ϖ(Σθ: str) -> int:
            ϡΞ: int = 0
            Ψβ: int = 0
            ϔΠ: int = 0
            while Ψβ < len(Σθ):
                if ƝɃ(Σθ[Ψβ]):
                    ϡΞ += 1
                    ϔΠ = Ƭἴ(ϡΞ, ϔΠ)
                else:
                    ϡΞ = Οκ(ϡΞ, 1)
                Ψβ += 1
            return ϔΠ

        return ϖ(group_string)

    ơʔʭ: List[int] = []

    def κıΞ(φιχϵs: List[str], βîrΛ: int) -> List[int]:
        if βîrΛ >= len(φιχϵs):
            return ơʔʭ
        else:
            if φιχϵs[βîrΛ] != "":
                ơʔʭ.append(parse_paren_group(φιχϵs[βîrΛ]))
            return κıΞ(φιχϵs, βîrΛ + 1)

    Ξ₊Ə: str = ""
    ℧₌ʬd: int = 0
    while ℧₌ʬd < len(parentheses_string):
        c = parentheses_string[℧₌ʬd]
        Ξ₊Ə += c if c != ' ' else '\0'
        ℧₌ʬd += 1

    χϝψ: List[str] = []
    λΒɶʭ: int = 0
    ζɮ: int = 0
    while ζɮ <= len(Ξ₊Ə):
        if ζɮ == len(Ξ₊Ə) or (ζɮ < len(Ξ₊Ə) and Ξ₊Ə[ζɮ] == '\0'):
            χϝψ.append(Ξ₊Ə[λΒɶʭ:ζɮ])
            λΒɶʭ = ζɮ + 1
        ζɮ += 1

    return κıΞ(χϝψ, 0)