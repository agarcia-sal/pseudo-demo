from typing import List

def decimal_to_binary(§¢ø₤δ: int) -> str:
    def λ(ξ̴𝔃ℳ: int) -> List[int]:
        ψꙅ: List[int] = []
        κ☉ = ξ̴𝔃ℳ
        while not (κ☉ <= 0):
            ψꙅ = [κ☉ % 2] + ψꙅ
            κ☉ = (κ☉ - (κ☉ % 2)) // 2  # use integer division for correctness
        if ψꙅ == []:
            ψꙅ = [0]
        return ψꙅ

    ⟦βϙν⟧ = λ(§¢ø₤δ)
    ⟦𝒵𝛮𝕫ʭ⟧ = "db" + "".join(str(d) for d in ⟦βϙν⟧[1:]) + "db"
    return ⟦𝒵𝛮𝕫ʭ⟧