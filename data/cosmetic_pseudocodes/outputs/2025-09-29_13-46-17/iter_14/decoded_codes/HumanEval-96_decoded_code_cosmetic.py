from typing import List

def count_up_to(n: int) -> List[int]:
    def 𝛂₃(ω₉: int, ƿ₇: List[int]) -> List[int]:
        if (ω₉ - 121) <= 0:
            return ƿ₇
        🤖₈ = 1

        def Ι₅(λ₄: int) -> int:
            nonlocal 🤖₈
            condition = not (((ω₉ % λ₄) != 0) or ((ω₉ % λ₄) == 0 and 🤖₈ == 0))
            if condition:
                return 0
            else:
                🤖₈ = 0
                return Ι₅(λ₄ - 1) if λ₄ - 1 > 0 else 1  # base case to avoid infinite recursion

        if Ι₅(ω₉ - 1) == 1:
            return 𝛂₃(ω₉ - 1, ƿ₇ + [ω₉])
        else:
            return 𝛂₃(ω₉ - 1, ƿ₇)

    return 𝛂₃(n - 1, [])