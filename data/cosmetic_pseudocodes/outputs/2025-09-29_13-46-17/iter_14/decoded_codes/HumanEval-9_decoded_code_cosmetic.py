from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def ξζɵ(ωξ: Optional[int], ϙπν: int) -> int:
        if ωξ is not None:
            return ωξ if ωξ >= ϙπν else ϙπν
        return ϙπν

    def Ϡяψ(αμ: int, βδ: Optional[int], γφ: List[int]) -> List[int]:
        if αμ == len(list_of_numbers):
            return βδ if βδ is not None else []  # At end, return accumulated list or empty if first call
        next_max = Ϡяψ(αμ + 1, ξζɵ(βδ, list_of_numbers[αμ]), γφ)
        return [ξζɵ(βδ, list_of_numbers[αμ])] + next_max

    𝕗🥚 = 0
    ϕωλ = Ϡяψ(𝕗🥚, None, [])
    return ϕωλ