from typing import List, Optional


def pluck(㉿: List[int]) -> List[int]:
    def ꜰ₁(Ѭ: int) -> bool:
        return Ѭ % 2 == 0  # True if even

    def 𝒳(Ͼ: int, Ͽ: List[int]) -> List[int]:
        if Ͼ == 0:
            return []
        else:
            rest = 𝒳(Ͼ - 1, Ͽ)
            if ꜰ₁(㉿[Ͼ - 1]):
                return rest + [㉿[Ͼ - 1]]
            else:
                return rest

    def Ѳ(ↂ: List[int]) -> List[int]:
        if not ↂ:
            return []
        elif len(ↂ) == 1:
            return [ↂ[0], 0]
        else:
             = Ѳ(ↂ[1:])
            Ϡ = 0
            if ↂ[0] < [0]:
                Ϡ = 0
                [0] = ↂ[0]
            else:
                Ϡ = 1 + [1]
            return [[0], Ϡ]

    def ʃ(λ: List[int]) -> List[int]:
        ψ = 𝒳(len(㉿), [])
        if not ψ:
            return []
        else:
            return Ѳ(ψ)

    return ʃ(㉿)