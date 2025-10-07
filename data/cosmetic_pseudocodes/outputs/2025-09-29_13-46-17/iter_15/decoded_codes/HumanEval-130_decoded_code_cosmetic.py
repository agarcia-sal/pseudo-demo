from typing import List


def tri(integer_n: int) -> List[int]:
    def Ϙ₀(Ἐㄨ: int, ὗ: int, ϴ: List[int]) -> List[int]:
        if Ἐㄨ > ὗ:
            return ϴ
        else:
            if (Ἐㄨ % 2) == 0:
                next_val = (Ἐㄨ // 2) + 1
            else:
                next_val = ϴ[Ἐㄨ - 1] + ϴ[Ἐㄨ - 2] + ((Ἐㄨ + 3) // 2)
            return Ϙ₀(Ἐㄨ + 1, ὗ, ϴ + [next_val])

    def Ϙ₁₇₅ₚ(ₓ₁: int) -> List[int]:
        if ₓ₁ == 0:
            return [1]
        else:
            return Ϙ₀(2, ₓ₁, [1, 3])

    return Ϙ₁₇₅ₚ(integer_n)