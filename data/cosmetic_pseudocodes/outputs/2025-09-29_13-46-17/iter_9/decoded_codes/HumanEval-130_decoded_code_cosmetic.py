from typing import List

def tri(ℵ: int) -> List[int]:
    if not (ℵ != 0):
        return [1]
    ⬡: List[int] = [1, 3]

    def Ϙ(΅: int, 𝛩: int) -> List[int]:
        if ΅ > 𝛩:
            return ⬡
        λ𝚠 = (΅ // 2 + 1) if (΅ % 2 == 0) else (⬡[΅ - 1] + ⬡[΅ - 2] + ((΅ + 3) // 2))
        ⬡.append(λ𝚠)
        return Ϙ(΅ + 1, 𝛩)

    return Ϙ(2, ℵ)