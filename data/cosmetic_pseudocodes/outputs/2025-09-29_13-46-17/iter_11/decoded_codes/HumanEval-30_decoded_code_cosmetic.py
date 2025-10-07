from typing import List

def get_positive(Ω7Ϭ: List[int]) -> List[int]:
    def Яβ(Ξ1: List[int], ϱ: int) -> List[int]:
        if ϱ > 0:
            return Ξ1 + [ϱ]
        return Ξ1

    def Ҕχ(ƛε: int, ϟӼ: List[int]) -> List[int]:
        if ƛε == 0:
            return []
        return Яβ(Ҕχ(ƛε - 1, ϟӼ), ϟӼ[ƛε - 1])

    return Ҕχ(len(Ω7Ϭ), Ω7Ϭ)